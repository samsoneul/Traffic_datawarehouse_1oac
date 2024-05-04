{{ config(materialized='table') }}

WITH route_analysis AS (
    SELECT
        lat,
        lon,
        COUNT(*) AS frequency
    FROM
        "Trajectory_Data"
    GROUP BY
        lat,
        lon
    ORDER BY
        frequency DESC
)

SELECT * FROM route_analysis
