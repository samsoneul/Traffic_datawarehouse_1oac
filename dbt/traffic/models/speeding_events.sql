{{ config(materialized='table') }}

WITH speeding_events AS (
    SELECT
        track_id,
        lat,
        lon,
        speed
    FROM
        "Trajectory_Data"
    WHERE
        CAST(speed AS numeric) > 80
)

SELECT * FROM speeding_events
