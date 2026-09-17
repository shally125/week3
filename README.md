# The phenomenon

<!-- This is the SD5913 assignment 2 template. Everything in this file is yours to
replace, and the check counts words: comments like this one are not words, so
delete each one as you write. Start with the heading: name the phenomenon.

Then, in this order, at least 150 words in total.

New to folders, paths, or the files here whose names start with a dot? Read
https://github.com/sd5913/pfad/blob/2026/reference/files.md first. Ten minutes. -->

![what the picture is](out/plot.png)

## The phenomenon

Greenhouse gases trap heat in the atmosphere and drive climate change. This project uses 35 years of Hong Kong measurements to make a circular portrait of how emissions and the carbon efficiency of the economy changed. I chose the artist's path: the numbers are the material of one image.

## The source

The raw file is the HKSAR Government's [Greenhouse Gas Emissions and Carbon Intensity JSON](https://cnsd.gov.hk/wp-content/uploads/pdf/greenhouse_gas_emissions_and_carbon_intensity.json). It contains 35 annual records from 1990 to 2024. Every record contains total greenhouse gas emissions in kilotonnes of CO₂-equivalent, per-capita emissions in tonnes of CO₂-equivalent, and carbon intensity in kilograms of CO₂-equivalent per Hong Kong dollar of GDP. `fetch.py` requests the file once and preserves the raw reply in `data/`, so `plot.py` runs without an internet connection.

## What the picture shows

Time travels clockwise around the flower, beginning with 1990 at the top. Each petal is one year. Its length comes from total emissions, its width from emissions per person, and its colour from carbon intensity: warm orange marks higher intensity and teal marks lower intensity. The movement from warm to cool colour shows the long decline in carbon intensity, which fell about 67% by 2024. The uneven outer edge records the much less direct path of total emissions.

## Run it

```
uv run fetch.py
uv run plot.py
```
