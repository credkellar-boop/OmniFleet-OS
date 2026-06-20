package main

import (
	"log"
)

type TelemetryBuffer struct {
	Queue    []string
	Capacity int
	IsOnline bool
}

// Caches CAN bus and API metrics locally to prevent data loss
func (tb *TelemetryBuffer) BufferMetric(metric string) {
	if len(tb.Queue) >= tb.Capacity {
		tb.Queue = tb.Queue[1:] // Drop the oldest metric
	}
	tb.Queue = append(tb.Queue, metric)
}

func (tb *TelemetryBuffer) FlushToCloud() {
	if tb.IsOnline && len(tb.Queue) > 0 {
		log.Printf("Connection restored. Flushing %d telemetry packets to event stream...", len(tb.Queue))
		tb.Queue = nil
	}
}

func main() {
	buffer := TelemetryBuffer{Capacity: 10000, IsOnline: false}
	buffer.BufferMetric("BATTERY_TEMP: 34.2C")
}
