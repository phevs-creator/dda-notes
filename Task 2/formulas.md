# Formulas for Dashboard

<img width="1877" height="747" alt="image" src="https://github.com/user-attachments/assets/2905a5fc-c718-466e-a5d3-ec8da36d3507" />

---

<img width="1243" height="745" alt="image" src="https://github.com/user-attachments/assets/0c5f3efd-95d7-4372-a8aa-ee1034be21cf" />

##### Age Range formula:

> =SWITCH(TRUE, [@[Age Group]]="", "N/A", [@[Age Group]]<25, "25<", [@[Age Group]]<41, "25-40", [@[Age Group]]<56, "41-55", [@[Age Group]]<71, "56-70", [@[Age Group]]<86, "70+")

##### Month/Year Formula:

> =DATE(YEAR([@Date]), MONTH([@Date]), 1)

<p>These two formulas gives more ways for analysis to be done. The Age Range makes it easier to sort the ages and so their are not too many different values, because analysis would then be unsuitable. The Month/Year column will allow for better analysis in the calculating table.</p>

<p>The other areas we use formulas for is in the calculation page. This page acts as a basis for the reactive dashboard and helps to to show different filters, overall statistics and values specific to each variable.</p>

##### Month and Year Spill Formula:

> =EDATE(E2,SEQUENCE(DATEDIF(E2,E3, "m")+1,1,0))

<p>This formula consists of the EDATE formula, SEQUENCE formula and DATEDIF formula. The E2 cell shows the lowest selected Month and E3 shows the highest selected date.</p>

##### Month Count Formula:

> =COUNTIFS(Append1[Month/Year], D11, Append1[Location], $E$4, ...)

<p>This formula filters the months by the month cell (D11). The Location filter shows the other filters that can be applied and more can be added. This is the only filter that uses the easier date filter.</p>

##### Other Filter Formula:

> =COUNTIFS(Append1[Date], ">="&$B$2, Append1[Date], "<="&$B$3, Append1[Location], H11, ...)

<p>The two date filters are done through using the date formula, making a more than or less than condition, using & to add it to a criteria and then specifing the date from/to cell. In this example, $B$2 is the date filtered from (lowest possible date) and $B$3 is the opposite.</p>