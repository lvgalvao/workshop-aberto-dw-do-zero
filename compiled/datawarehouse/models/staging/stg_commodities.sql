-- models/staging/stg_commodities.sql

with source as (
    select
        "Date",
        "Close",
        simbolo
    from 
        "databasesales"."public"."commodities"
),

renamed as (
    select
        cast("Date" as date) as data,
        "Close" as valor_fechamento,
        simbolo
    from source
)

select
    data,
    valor_fechamento,
    simbolo
from renamed