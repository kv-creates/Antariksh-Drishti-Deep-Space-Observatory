# 🗓️ Scheduling

![Schedule](../docs/images/schedule-gantt.png)

Greedy by priority (`src/scheduler.py:schedule`):

1. Sort descending `priority`
2. Require `sun > 85°` (`sun_ok`)
3. Require `saa_free(lat, lon)` — reject SAA box (-30<lat<10, -60<lon<-20)
4. Append with 5-min slew; efficiency = scheduled/requested

```python
from src.scheduler import schedule
schedule([{"id":"TOI-715 b","priority":9.2,"duration":60,"sun":120}])
```

See `examples/schedule_example.py` and `docs/operations.md`.
