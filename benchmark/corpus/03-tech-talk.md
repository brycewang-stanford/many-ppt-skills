# Corpus 03 — Conference Tech Talk

**Stresses:** code blocks · architecture diagrams · progressive build-up · monospace typography
**Target length:** 18–22 slides
**Audience:** engineers at a systems conference, 25-minute slot, projected in a dim room
**Failure modes this corpus exposes:** code that overflows or loses syntax highlighting,
diagrams rendered as unreadable text blobs, no visual distinction between narrative and
code slides, slides too dense to read from row 20

> All content below is fictional. The system described is invented test material.

---

## Brief

A 25-minute conference talk: "Backpressure Without Buffers — What We Learned Rewriting
Our Ingest Pipeline". Speaker-led, so slides should punctuate rather than narrate. Code
must be legible from the back of a room: large monospace, short excerpts, one idea per
listing.

**Hard requirement:** every code listing must appear with syntax highlighting and correct
indentation. Code rendered as an image, or reflowed so indentation is lost, scores zero
on data fidelity.

---

## Content

### Title

**Backpressure Without Buffers**
What we learned rewriting our ingest pipeline

Ana Restrepo · Systems Conf 2026 *(fictional speaker)*

### The setup

We ingest telemetry from roughly 90,000 devices. Each emits a batch every 15 seconds.
Peak load is 2.1M events per second. The old pipeline was three services connected by
two queues, and it worked fine for four years.

### Until it didn't

One Tuesday a firmware rollout doubled the emit rate on 30,000 devices simultaneously.

The queues absorbed it. That was the problem.

### What actually happened

```
producers ──▶ [ queue A ] ──▶ transform ──▶ [ queue B ] ──▶ writer ──▶ storage
                 8 GB                          32 GB
```

Queue A filled in 90 seconds. Queue B filled in 6 minutes. By the time the writer's
latency alarm fired, we had 40 GB of buffered events and no way to tell how old any
of them were. Recovery took 4 hours, most of it spent draining data that was already
stale and would be discarded downstream anyway.

### The lesson

> A buffer does not solve overload. It converts an immediate, visible failure into
> a delayed, invisible one.

### What we wanted instead

Three properties:

1. **Load shedding is explicit.** When we cannot keep up, we decide what to drop and
   we say so — not the queue's eviction policy at 3am.
2. **Latency is bounded.** An event is either processed within its freshness window or
   discarded. There is no third state.
3. **Pressure propagates.** A slow writer must be felt by the producer, not absorbed
   silently between them.

### The core idea

Replace the queue with a bounded channel that refuses writes instead of growing.

```rust
// A channel that refuses rather than buffers.
// try_send returns immediately — it never blocks and never grows.
let (tx, rx) = bounded::channel(capacity: 1024);

match tx.try_send(event) {
    Ok(()) => metrics.accepted.inc(),
    Err(TrySendError::Full(ev)) => {
        // We are behind. Decide here, explicitly, in the open.
        metrics.shed.inc();
        shed_policy.record(ev);
    }
}
```

That `Err` arm is the entire design. It is the place where overload becomes a decision
instead of an accident.

### Shedding is a policy, not an accident

Not all events are equal. We classify at the edge:

```rust
enum Priority {
    Critical,   // alarms, state transitions — never shed
    Standard,   // routine telemetry — shed under pressure
    Bulk,       // diagnostics — shed first
}

fn should_shed(p: Priority, pressure: f32) -> bool {
    match p {
        Priority::Critical => false,
        Priority::Standard => pressure > 0.85,
        Priority::Bulk     => pressure > 0.40,
    }
}
```

Bulk telemetry starts dropping at 40% pressure. Critical events never drop. Under the
firmware incident, this would have shed 61% of volume and kept every alarm.

### Propagating pressure upstream

The producer polls a pressure signal and adjusts its own emit rate:

```rust
// Producers read pressure and back off before the channel refuses them.
// Additive increase, multiplicative decrease — the same shape as TCP congestion control.
let pressure = pipeline.pressure();          // 0.0 ..= 1.0

let interval = if pressure > 0.7 {
    self.interval * 2                        // back off hard
} else {
    (self.interval - Duration::from_millis(50))
        .max(BASE_INTERVAL)                  // recover gently
};
```

### The new topology

```
producers ◀── pressure signal ──────────────┐
    │                                       │
    └──▶ [ bounded 1024 ] ──▶ transform ──▶ [ bounded 1024 ] ──▶ writer ──▶ storage
              │                                   │
              └──▶ shed ──▶ counters              └──▶ shed ──▶ counters
```

Total buffering: 2048 events, about 40 milliseconds at peak. Down from 40 GB.

### Results

| Metric | Before | After |
|---|---:|---:|
| p99 end-to-end latency | 4.2 s | 180 ms |
| Worst-case buffered data | 40 GB | 2048 events |
| Recovery time from 2x overload | 4 hrs | 90 s |
| Events dropped during overload | 0 (all stale) | 61% (all low-priority) |

We now drop more data and deliver far more value. That is not a paradox — the dropped
data was already worthless by the time the old system delivered it.

### What we got wrong

**We set the first capacity to 64.** Too tight. Normal jitter triggered shedding, and
we spent two weeks chasing phantom load. Capacity should absorb jitter, not load —
we sized it at roughly 2x the p99 batch arrival burst and stopped tuning.

**We shipped without shed observability.** For a month we knew *that* we shed but not
*what*. Per-priority, per-source shed counters should have been in the first commit.

### Takeaways

1. Buffers hide overload. Bounded channels surface it.
2. Shedding is a product decision. Write it down, make it explicit, make it visible.
3. Backpressure that stops at a queue boundary is not backpressure.

### Close

**Backpressure Without Buffers**
Ana Restrepo · questions welcome
