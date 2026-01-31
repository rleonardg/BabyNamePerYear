# BabyNamePerYear - Data Analytics
>*_Summary: Recopilation of the most common names._*

| Requirements | Skills |
|--------------|--------|
| - `python3.10`<br> - `pandas`<br> - `excel`<br> - `power query`<br> - `Tableau`  |  - `Dashboard design (Tableau)`<br> - `Data cleaning and transformation`<br> - `Data wrangling`<br> - `YoY KPI calculation` |

## Usage

### HowManyNamesByYear 
Select the most n common names for the sex selected from the dataset baby_names.csv.

#### Example
```bash
python3 HowManyNamesByYear "csv_baby_names__path.csv" 100 'F'
```

## Visualization

### 01. Wide Format
Wide format is the default format of baby_names_result.csv. This format works with tools such as Flourish. You can see the dinamic graphic in flourish [here](https://public.flourish.studio/visualisation/27433129/)
<img src="https://github.com/rleonardg/BabyNamePerYear/assets/flourish_dynamic_bar_image.png">

### 02. Long Format
The Long Format is the common format for tools such as Power BI and tableau. Can be obtain by ['unpivot columns'](https://support.microsoft.com/en-us/office/unpivot-columns-power-query-0f7bad4b-9ea1-49c1-9d95-f588221c7098) excel option.


## Resources
- [SSA](https://www.ssa.gov/oact/babynames/)
