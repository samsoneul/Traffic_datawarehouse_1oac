{{ config(materialized='table') }}

WITH distance_summary AS (
    SELECT
        fs.full_distance,
        fs.type,
        COUNT(fs.track_id) AS count,
        AVG(CAST(fs.total_time AS numeric)) AS avg_duration,
        AVG(CAST(fs.avg_speed AS numeric)) AS avg_speed,
        AVG(CAST(ts.max_speed AS numeric)) AS max_speed,
        AVG(CAST(fs.max_lat_acc AS numeric)) AS max_lat_acc,
        AVG(CAST(fs.max_lon_acc AS numeric)) AS max_lon_acc
    FROM
        {{ ref('full_summary') }} fs
    JOIN
        {{ ref('trajectory_summary') }} ts ON fs.track_id = ts.track_id
    GROUP BY fs.full_distance, fs.type
)
SELECT * FROM distance_summary
