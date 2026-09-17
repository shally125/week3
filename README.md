# The phenomenon

<!-- This is the SD5913 assignment 2 template. Everything in this file is yours to
replace, and the check counts words: comments like this one are not words, so
delete each one as you write. Start with the heading: name the phenomenon.

Then, in this order, at least 150 words in total.

New to folders, paths, or the files here whose names start with a dot? Read
https://github.com/sd5913/pfad/blob/2026/reference/files.md first. Ten minutes. -->

![what the picture is](out/plot.png)

## The phenomenon

Greenhouse gases trap heat in the atmosphere and drive climate change. This project examines how Hong Kong's emissions changed between 1990 and 2024. I was especially interested in whether the economy became less carbon-intensive and whether that improvement was matched by similar reductions in the city's total and per-capita emissions.

## The source

The raw JSON is published by the HKSAR Government's Carbon Neutrality and Sustainable Development Office: [Greenhouse Gas Emissions and Carbon Intensity](https://cnsd.gov.hk/wpcontent/uploads/pdf/greenhouse_gas_emissions_and_carbon_intensity.json).

The cached file contains 35 annual records. Each record gives the report year, total greenhouse gas emissions in kilotonnes of carbon-dioxide equivalent, emissions per person in tonnes of CO₂-e, and carbon intensity in kilograms of CO₂-e per Hong Kong dollar of GDP. 

## What the picture shows

<!-- Two or three sentences. Including what it hides: every transformation throws
something away, and naming what yours threw away is the easiest way to sound like
you know what you did. -->

## Run it

```
uv run fetch.py
uv run plot.py
```
