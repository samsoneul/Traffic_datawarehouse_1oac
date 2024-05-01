-- models/transformed_trajectory_data.sql

-- Description: This model performs transformations on the Trajectory_Data table.

-- Define the model
{{ config(
    materialized='table',
    schema='analytics'
) }}

-- Perform transformations on Trajectory_Data and create a new table
SELECT
    column1,
    column2,
    column3
FROM
    {{ ref('public', 'Trajectory_Data') }}
