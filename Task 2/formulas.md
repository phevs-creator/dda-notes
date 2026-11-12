# Formulas for Dashboard

<img width="1877" height="747" alt="image" src="https://github.com/user-attachments/assets/2905a5fc-c718-466e-a5d3-ec8da36d3507" />

---

<img width="1243" height="745" alt="image" src="https://github.com/user-attachments/assets/0c5f3efd-95d7-4372-a8aa-ee1034be21cf" />

Age Range formula

> =SWITCH(TRUE, [@[Age Group]]="", "N/A", [@[Age Group]]<25, "25<", [@[Age Group]]<41, "25-40", [@[Age Group]]<56, "41-55", [@[Age Group]]<71, "56-70", [@[Age Group]]<86, "70+")

<br>

Month/Year Formula

> =DATE(YEAR([@Date]), MONTH([@Date]), 1)

<br>

<p>These two formulas gives more ways for analysis to be done. The Age Range makes it easier to sort the ages and so their are not too many different values, because analysis would then be unsuitable. The Month/Year column will allow for better analysis in the calculating table.</p>
