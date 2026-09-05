# Thread 2: Gender Injustice — Observations

---

## CSV 1 Analysis

### 01. Crimes Against Women by Category (2001–2022) — Multi-line

**Observations:**
- Cruelty by Husband or Relatives is the dominant crime category throughout, reaching ~1.4L by 2022 — it has never dipped below first rank in 22 years.
- Kidnapping & Abduction shows the steepest absolute rise — from ~14K in 2001 to ~85K in 2022, overtaking Assault on Women around 2014.
- Rape holds a relatively flat-to-moderate trend until the 2013 spike (~37K), then drops and stabilises around 31–32K post-2017.
- Immoral Traffic (P) Act and Importation of Girls are nearly invisible at the bottom — both are essentially extinct as reported crime categories.
- The bottom cluster (Dowry Deaths, Insult to Modesty, Immoral Traffic, Indecent Representation) has barely moved in 22 years, suggesting either stable rates or consistent under-reporting.

---

### 02. Composition of Crimes Against Women — Stacked Area (2001–2022)

**Observations:**
- Cruelty by Husband and Assault on Women dominate total volume — together they account for well over 50% of all crimes in any given year.
- The 2013 step-up is visible across almost every category simultaneously, confirming it is a reporting/definitional change, not a single-crime spike.
- Kidnapping & Abduction (green layer) is visibly growing as a share over time — it takes up noticeably more area in 2022 than in 2001.
- Rape (red) is a thin but persistent band; its share has not grown relative to total crimes despite the absolute numbers rising.
- The 2020 dip is visible as a slight constriction in the total stack — COVID lockdown suppressed reporting across all categories, not selectively.

---

### 03. Total Crimes Against Women — Annotated Trend (2001–2022)

**Observations:**
- Total crimes nearly doubled from ~1.45L in 2001 to ~3.7L in 2022.
- The sharpest single-year jump is 2012→2013 (~2.5L to ~3.1L), correctly annotated as the post-Nirbhaya and Criminal Law Amendment Act effect. This is largely a reporting surge, not a crime surge — the law broadened definitions and reduced barriers to filing FIRs.
- After 2014, the trend plateaus between 3.1–3.5L for several years, suggesting the reporting spike levelled off rather than reflecting a genuine crime wave.
- The 2020 COVID dip (~3.1L) is the only meaningful decline in 22 years — and it snaps back sharply in 2021–2022, confirming it was suppression of reporting rather than actual reduction.
- 2022 hits the highest point in the dataset at ~3.7L.

---

### 04. Percentage Change in Crimes 2001 vs 2022 — Bar Chart

**Observations:**
- Kidnapping & Abduction registered the highest growth at +482.5% — by far the largest change of any category, nearly 5x over 22 years.
- Dowry Prohibition Act cases rose +318.3% — this is likely increased enforcement/filing activity, not simply more dowry, since Dowry Deaths (the outcome measure) actually fell -5.9%.
- Cruelty by Husband (+184.8%) and Assault on Women (+144.2%) show substantial growth but less dramatic than kidnapping.
- Rape +96.1% — roughly doubled over 22 years, but important context: definitional expansion in 2013 inflates the post-2013 numbers.
- Importation of Girls (-99.1%), Indecent Representation (-97.3%), and Immoral Traffic (-83.0%) all collapsed — likely a combination of law enforcement reprioritisation and category reclassification rather than genuine eradication.
- The divergence between Dowry Deaths (-5.9%) and Dowry Prohibition Act cases (+318.3%) is analytically important: prosecutions are rising even as deaths fall, suggesting enforcement is catching earlier-stage violations.

---

## CSV 2 Analysis

### 05. Total Crimes by State/UT (2022) — Bar Chart

**Observations:**
- Uttar Pradesh leads by a wide margin at 65,743 — more than 40% higher than the next state.
- Maharashtra (45,331) and Rajasthan (45,058) are nearly tied for second.
- West Bengal (34,738) and Madhya Pradesh (32,765) round out the top 5.
- Tamil Nadu (9,207) is conspicuously low for a large, highly urbanised state — likely reflects under-reporting or definitional differences in data collection.
- Delhi (14,247) appears low relative to its crime rate per lakh (186.9 from CSV4) — because this is absolute numbers and Delhi's population is smaller than UP or Maharashtra.

---

### 06. Total Crimes by State/UT (2020) — Bar Chart

**Observations:**
- UP still dominates at ~49K but the gap with other states is smaller than in 2022.
- West Bengal was second in 2020 at 36K — it drops to 4th by 2022, suggesting either genuine improvement or reporting pattern change.
- Assam (26,352) appears in the top 5 in 2020 but falls out by 2022 — needs checking whether this is a real trend or a data artefact.
- The overall national totals are lower in 2020 vs 2022, consistent with COVID lockdown suppressing reporting across states.

---

### 07. Total Crimes by State/UT (2001) — Bar Chart

**Observations:**
- UP was already #1 in 2001 at ~19.9K — it has held the top spot for the entire 22-year period.
- Andhra Pradesh (15,919) was a distant second — by 2022 it has fallen to 6th. Its growth (+60%) is among the lowest of any large state.
- Tamil Nadu (10,064) was in the top 6 in 2001 but ranks near the bottom in 2022 by absolute numbers — a genuine outlier worth flagging.
- The entire top 15 in 2001 had lower numbers than UP's 2022 number alone.

---

### 08. State × Crime Head Heatmap (2014, Standardized Categories)

**Observations:**
- Kidnapping & Abduction is the darkest column for UP (21,252) and West Bengal (9,952) — these two states account for an outsized share of this crime nationally.
- Cruelty & Dowry Offenses is the darkest column for West Bengal (23,781) — higher than UP (15,139) despite WB having lower total crimes. This is a state-specific pattern worth highlighting.
- MP has the highest Rape & Attempted Rape numbers (15,284) among the top 15 states in 2014 — higher even than UP, which has 10,725.
- Maharashtra has the highest Special & Local Laws count (986) — suggesting more active enforcement of supplementary statutes.
- Human Trafficking numbers are small across all states, but Karnataka (776) and Andhra Pradesh (408) are disproportionately high relative to their total crimes.

---

### 09. Top 5 States — Crime Trend Grid (2001–2022)

**Observations (reading past the truncation bug):**
- All five states show the characteristic 2013 jump clearly — confirms this is a national phenomenon, not state-specific.
- UP's trend is the most volatile — it dips significantly in 2014–2015 before rising again, which may reflect data quality issues or a real policing shift.
- West Bengal peaks sharply in 2014–2015 then partially declines — unlike the other four which keep rising.
- Rajasthan shows the most erratic pattern — multiple spikes and drops — possibly reflecting inconsistent reporting rather than real volatility.
- Maharashtra and MP both show sustained upward trends with no meaningful dip other than 2020.

---

### 10. All India vs Delhi / UP / Rajasthan — Line Chart

**Observations:**
- All India total is consistently ~5–6x the sum of the three states shown, which makes sense given ~28 states contribute.
- UP's line tracks closest to All India in shape — the 2013 jump, the 2020 dip, the 2021–2022 recovery all mirror the national trend. This confirms UP's outsized influence on national statistics.
- Rajasthan's post-2013 number (~45K) is close to Delhi's entire annual total, despite Rajasthan being less urbanised. High rate per population.
- Delhi remains the smallest absolute numbers of the three but is densest per capita.

---

### 11. State Bar 2022 with % Change Since 2001

**Observations:**
- Lakshadweep shows `+inf%` — this is because its 2001 count was 0. Needs handling: either exclude Lakshadweep or display "N/A (no 2001 data)" instead of +inf%.
- Meghalaya (+945%) and Sikkim (+646%) and Delhi (+524%) have the highest growth rates — but from very small 2001 bases, so percentages are not directly comparable to large-state growth.
- Tamil Nadu is the only state with a negative growth rate (-9%) — unique and worth calling out. Either it genuinely improved or there's a reporting/definitional issue.
- Andhra Pradesh (+60%) has the lowest growth among large states — possible under-reporting, or bifurcation with Telangana in 2014 splitting its numbers.
- West Bengal's +429% growth despite a moderate 2022 absolute count suggests it started from a very low base.

---

## CSV 3 Analysis

### 12. Conviction Rate (%) by State/UT

**Observations:**
- Nagaland (83.3%) leads conviction rates — but has only 287 total cases for trial, so the denominator is tiny and the rate is not robust.
- Mizoram (69.8%) and UP (64.6%) follow — UP's high conviction rate is striking given its high absolute crime volume.
- The bottom states are Karnataka (3.2%), West Bengal (3.7%), J&K (3.8%), AP (5.8%) — all large, populous states with significant judicial infrastructure but abysmal conviction rates.
- The national average is 21.3%, meaning nearly 4 out of 5 completed trials end without conviction.
- Bihar's 56.3% appears high but is misleading — Bihar has a 98% pendency rate, meaning only 2,282 trials were completed out of 133K cases for trial. The conviction rate looks good only because the courts barely try any cases.

---

### 13. Judicial Backlog — Pendency % by State/UT

**Observations:**
- Bihar tops the pendency chart at 98% — meaning 98 of every 100 cases remain pending at year-end. This is a near-complete judicial freeze.
- Every state shown has 92–98% pendency — the variation within this range is almost meaningless. The story is that there is no state where the courts are keeping up.
- Maharashtra (95.1%) has 2.93 lakh cases pending despite having substantial court infrastructure — suggesting the *volume* of crime overwhelms any capacity advantage.
- The top 15 most-pending states include both small NE states (Manipur, Arunachal, Nagaland) and large states (Maharashtra, WB, Odisha, UP) — pendency is not a small-state problem, it is systemic.

---

### 14. Conviction Rate vs Pendency % — Scatter Plot

**Observations:**
- No clear negative correlation between pendency and conviction rate — the points are scattered. High-pendency states can have either high or low conviction rates.
- Bihar and Nagaland occupy the top-right (high pendency, high conviction) — but for opposite reasons: Bihar barely completes trials (small denominator), Nagaland has small total case numbers.
- West Bengal and Karnataka are bottom-right (high pendency, very low conviction) — the worst possible combination.
- UP is an outlier in the middle-right — high pendency (92.4%) but unusually high conviction (64.6%), suggesting when trials do complete in UP, they skew heavily toward conviction.
- Mizoram sits at mid-x (~83% pendency) but very high conviction (~70%) — genuinely outperforming its peers where trials complete.

---

### 15. Case Disposition Pipeline — Stacked Bar (Normalised 100%)

**Observations:**
- The dark navy (Pending Cases) dominates every bar — in most states it's 85–97% of the total. The justice system's primary output for crimes against women is: wait.
- Bihar's bar is almost entirely navy with a tiny sliver of anything else — consistent with the 98% pendency stat.
- Telangana and Andhra Pradesh have the largest purple segments (Cases Compounded/Compromised) — suggesting out-of-court settlement or withdrawal is more common in these states, which is concerning for victim outcomes.
- Assam has a visible purple band (Withdrawn from Prosecution) — cases are being dropped at an institutional level, not even reaching trial.
- MP's bar shows the most variety — some acquittals, some discharges, some compounding — suggesting more cases actually make it to various stages, even if conviction is still rare.

---

## CSV 4 Analysis

### 16. Crime Rate vs Chargesheet Rate — Bubble Chart (2022)

**Observations:**
- Jaipur is an extreme outlier — highest crime rate at 239.3 per lakh, and lowest chargesheet rate at 53%. High crime, low follow-through from police. A broken accountability signal.
- Delhi City has the second-highest crime rate (186.9) and a moderate chargesheet rate (72.4%) — large volume, average police follow-through.
- Indore has 174.3 crime rate and 75.9% chargesheet rate — high crime but better than Jaipur on police response.
- Patna has the highest chargesheet rate (93.2%) and a moderate crime rate (84.7) — suggesting active police chargesheeting relative to FIRs.
- Cities like Kolkata (27.8 crime rate, 86.9% chargesheet) and Chennai (17.1, 81.1%) are in the "low crime, decent response" quadrant.
- Ghaziabad (96.5 per lakh) is striking for a satellite city — comparable to Bengaluru and significantly higher than Mumbai.
- The viridis colour scale encodes chargesheet rate — it reinforces the pattern but a legend explaining this would help.

---

### 17. Post-COVID Crime Recovery (2020 vs 2021 vs 2022) — Grouped Bar

**Observations:**
- Delhi City is dominant at ~14K in 2022, more than double Mumbai (~6.1K). The scale difference makes the rest of the chart hard to read — consider log scale or splitting Delhi into a separate panel.
- Ghaziabad shows the sharpest growth trajectory: 341 (2020) → 591 (2021) → 1,063 (2022) — roughly tripling over three years. Most cities recovered to near-2019 levels; Ghaziabad went well past them.
- Kanpur shows an unusual pattern — it peaks in 2022 at ~2,099 while 2021 was only 894, an anomalous jump that may reflect a data quality issue or a genuine enforcement push.
- Coimbatore is barely visible — too small to read on this scale. The chart is dominated by top-4 cities.
- All cities show 2022 > 2021 > 2020, confirming the post-COVID reporting recovery is near-universal.

---

### 18. Crime Rate per Lakh Across Cities (2022) — Bar Chart

**Observations:**
- Jaipur (239.3) leads by a significant margin — a rate nearly 14x Chennai (17.1) and nearly 19x Coimbatore (12.9).
- The top 5 (Jaipur, Delhi, Indore, Lucknow, Kanpur) are all North/Central Indian cities. No South Indian city appears in the top 10.
- Ghaziabad (96.5) is 8th — notable because it is a Tier-2 satellite city, not a metro. Its rate is comparable to Bengaluru (96.7).
- Mumbai (72.5) ranks 12th despite being India's largest city — suggesting either genuine better outcomes or systematic under-reporting.
- South Indian cities consistently cluster at the bottom: Chennai (17.1), Kozhikode (71.3), Kochi (70.1) — a regional pattern worth naming explicitly.

---

## CSV 4 + CSV 6 Cross-Dataset

### 19. Chargesheet Rate (2022) vs % 156(3) Cases (2023) — Scatter

**Observations (once fixed):**
- The negative trend line suggests cities where police resist filing FIRs (high 156(3) court-ordered cases) also have lower chargesheet rates — police are compelled to file but don't follow through.
- Cities clustering at the top-left (low 156(3), high chargesheet) are functioning normally — Patna, Kozhikode, Kochi.
- Jaipur, if its 156(3) rate is genuinely that high, would be the most extreme case of court-FIR dependency in the dataset.

---

## CSV 5 Analysis

### 20. Justice Pipeline: Arrested → Chargesheeted → Tried → Convicted (2023)

**Observations:**
- Delhi City's "Tried" bar (light blue) extends to ~1L — far larger than any other city, and visually dominates the chart. But the "Convicted" bar (red) is barely visible, suggesting an extremely low arrest-to-conviction conversion.
- For most cities, the yellow (Arrested) and orange (Chargesheeted) bars are nearly identical length — police are chargesheeting almost everyone arrested. The bottleneck is not chargesheeting, it is trials.
- Lucknow and Ahmedabad have anomalously long blue (Tried) bars relative to their arrested numbers — more trials completed than arrests in the same year, suggesting they are working through backlog from prior years.
- Bengaluru and Mumbai have large absolute numbers but the pipeline stages are more proportionate than Delhi.
- Srinagar, Patna, Lucknow: Convicted bars are 0 or invisible — zero convictions recorded despite significant arrest activity.

---

### 21. Gender Breakdown of Arrests (2023)

**Observations:**
- Male arrests dominate in every city — the female-arrested count (red bars) is consistently 10–20% of male arrests, meaning the perpetrators being arrested are overwhelmingly male as expected.
- Delhi City: 9,766 males arrested vs 1,584 females — the female count is likely co-accused (family members in cruelty/dowry cases) rather than primary perpetrators.
- Bengaluru and Mumbai have similar male-to-female ratios (~3:1 for female) — suggesting more family-based crimes being charged.
- Ghaziabad: 676 male, 0 female — the zero female arrest rate is unusual and may reflect how cases are being categorised.
- Transgender arrested count is effectively zero across all cities — either the data is not being collected or categorisation is absent.

---

### 22. Chargesheet-to-Arrest Ratio by City (2023)

**Observations:**
- Most cities cluster between 1.0–1.6 — relatively normal, suggesting chargesheeting tracks arrests reasonably closely.
- Vijayawada (17.15) and Vishakhapatnam (8.37) are severe outliers — both Andhra Pradesh cities, suggesting either a methodological difference in AP's data reporting or a genuine surge in chargesheeting of older arrests.
- Tiruchirapalli (0.39) and Madurai (0.58) are below 1 — police are arresting more people than they are chargesheeting, meaning cases are being dropped before formal charges.
- Bengaluru (0.98), Ghaziabad (0.93), Chennai (0.98) are all sub-1 — police are not converting all arrests to chargesheets.

---

### 23. Conviction Funnel Drop-off Rate by City (Convicted/Arrested %)

**Observations:**
- Meerut leads at 41.3% — extraordinarily high for this metric. Given that most cities are below 10%, this warrants investigation — it may reflect a small denominator (few arrests, many convictions from old cases).
- Ranchi (22.8%) and Kanpur (14%) are next — all UP/Jharkhand belt cities performing better than the national picture.
- Srinagar, Patna, Lucknow all show 0.0% — zero convictions per arrested persons in 2023. This is a complete justice system failure at the city level for these specific locations.
- Delhi (6.4%), Mumbai (1.7%), Bengaluru (0.6%) — India's three largest metros are in the bottom half. Bengaluru's 0.6% is alarming given its growing crime volume.
- The majority of cities (about 30 of 53) are below 3% — meaning fewer than 3 convictions per 100 arrests.

---

## CSV 6 Analysis

### 24. Total Crimes Against Women by City (2023) — All 53 Metro Cities

**Observations:**
- Delhi leads at 13,366 — more than double Mumbai (6,025) and nearly triple Bengaluru (4,870).
- The top 5 (Delhi, Mumbai, Bengaluru, Jaipur, Hyderabad) account for a disproportionate share of all metro city crimes.
- Vijayawada (2,221) ranking 8th is notable — it's not typically thought of as a high-crime city for women.
- The bottom of the chart (Tiruchirapalli 119, Coimbatore 244, Jamshedpur 266) are cities where crimes are reported at much lower rates — either genuinely safer or significant under-reporting.
- Ghaziabad (904) ranks 24th — lower in absolute terms but high in rate terms (as seen in CSV4).

---

### 25. % of 156(3) Court-Ordered FIRs by City (2023)

**Observations:**
- Asansol leads at 57.6% — meaning more than half of all FIRs in Asansol in 2023 were court-ordered rather than voluntarily registered by police. This is extraordinary and suggests police were systematically refusing to register FIRs, requiring survivors to go to court to compel registration.
- Jaipur (35.3%) and Jamshedpur (22.6%) follow — all three are cities where judicial intervention to force FIR registration is the norm, not the exception.
- The bottom ~30 cities show 0.0% — either they have no 156(3) cases, the data wasn't captured, or police compliance is complete. The 0.0% for major cities like Mumbai, Delhi, Gwalior, Meerut, Agra looks suspicious and may be a data reporting gap.
- The geographic concentration of 156(3) cases in specific cities (Asansol, Jaipur, Jamshedpur, Jodhpur) suggests this is a local institutional problem, not a national one.

---

## CSV 7 Analysis

### 26. Total Rape Cases by State/UT (2019) — Bar Chart

**Observations:**
- Rajasthan (5,902) leads by a wide margin — nearly double Uttar Pradesh (3,054) which is second despite UP being 2.5x larger by population.
- Madhya Pradesh (2,291) and Maharashtra (2,209) are almost equal in third and fourth.
- Kerala (1,934) appearing fifth is striking — Kerala consistently ranks high on social development indices, yet its rape reporting is among the highest. This is widely attributed to higher reporting rates and better access to police, not higher incidence.
- Large North-Eastern states like Manipur (36), Nagaland (5) have near-zero counts — almost certainly severe under-reporting rather than genuine safety.
- Bihar (730) is conspicuously low for India's third-most populous state — consistent with its systemic under-reporting across crime categories.

---

### 27. Composition of Rape Cases by Type — Stacked Bar (All States, 2019)

**Observations:**
- For Rajasthan and Madhya Pradesh, the dominant category is "Punishment for Rape" (the general/aggregate column) — their bars are overwhelmingly dark blue.
- UP has a distinct pattern: visible custodial rape segments (red shades) and a large gang rape (purple) component, setting it apart from other high-count states.
- Kerala's composition is heavily weighted toward "Relative/Guardian/Teacher/person in position of trust" — consistent with the interpretation that Kerala's numbers reflect better reporting of non-stranger rape, which is notoriously under-reported elsewhere.
- States like Jharkhand, Gujarat, Punjab, Delhi, West Bengal have large purple/navy segments (gang rape, girl below 16) — suggesting specific aggravated patterns.
- Assam has a visible pink segment (Jail/Remand staff) — notably different from most states, suggesting a custodial institutional problem.
- The chart is information-dense to the point of being hard to read — the legend has ~20 entries. Consider a simplified version grouping into 4–5 macro-categories for the final write-up.

---

### 28. Custodial Rape Breakdown by Subcategory (National, 2019)

**Observations (taking chart at face value):**
- "Repeated on same woman" (2,373) is the largest subcategory — meaning repeat perpetration on the same victim is more common than any other specific aggravated category nationally.
- "Relative/Guardian/Teacher/person in position of trust" (1,999) is second — trusted-person rape is nearly as common, confirming that stranger rape is a minority of reported cases.
- "Women Below 16" (790) is third — nearly 800 cases of rape of minors in a single year, nationally.
- Police personnel (5) and Armed Forces (1) are near-zero nationally — likely severe under-reporting given institutional pressure not to file.

---

### 29. Uttar Pradesh — Custodial Rape Subcategory Breakdown (2019)

**Observations:**
- UP's custodial rape is dominated by "Relative/Guardian/Teacher/person in position of trust" (27) — same pattern as the national level.
- "Management/Staff of Jail/Remand Home" (12) and "Public Servant" (10) are the next categories — indicating state employees committing rape in positions of power.
- Every other subcategory is zero for UP — including Police Personnel (0) and Armed Forces (0), which is implausible given UP's scale and is almost certainly under-reporting.
- The chart showing 0 for police in UP — a state with documented encounters, custodial deaths, and Hathras — is the finding itself.

---

### 30. Crimes Against Minors (Below 12 & Below 16) — Bar Chart

**Observations:**
- 790 cases of rape of women below 16 nationally — this is the largest bar and represents the "Punishment for Rape" threshold category.
- 170 cases of "Girl Below 16 Yrs (Imprisonment for life till death)" — these are the enhanced-punishment cases where the survivor is under 16.
- 47 cases of "Girl Below 12 Yrs" — the most severe category, carrying mandatory life imprisonment.
- The gap between 790 (generic below-16 reporting) and 170 (below-16 enhanced punishment invoked) suggests many cases where the victim's age qualifies for enhanced punishment but the enhanced provision wasn't invoked — a prosecution failure.
- These are national totals and almost certainly severe undercounts given the extremely low reporting rates for child sexual abuse in India.