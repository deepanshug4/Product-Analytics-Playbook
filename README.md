# 🍔 Product Analytics Playbook

A fictional food delivery platform built to demonstrate how Product Analysts use SQL and Python to solve real business problems.

---

## Project Goals

- Generate realistic synthetic marketplace data
- Analyze customer behaviour using SQL
- Visualize business metrics using Python
- Recommend product improvements

---

## Tech Stack

- Python
- SQL
- DuckDB
- Pandas
- Matplotlib

---

## Repository Structure

```text
src/
sql/
outputs/
case_studies/
```

---

## Business Questions

| Analysis | Business Question |
|-----------|------------------|
| Funnel | Where do users drop off? |
| Delivery Fee | Does delivery fee reduce conversion? |
| City | Which cities perform best? |
| Restaurant Quality | Do highly-rated restaurants convert better? |
| Coupons | Are coupons effective? |

---

## Example Output

<img width="2400" height="1500" alt="funnel_analysis" src="https://github.com/user-attachments/assets/c8614d6d-93df-4b9d-a486-30b342dc7846" />
<img width="1800" height="1200" alt="coupon_analysis" src="https://github.com/user-attachments/assets/5bb74591-7dc9-4fd1-aac6-7845cc6861a1" />
<img width="3000" height="1500" alt="city_performance" src="https://github.com/user-attachments/assets/2bf8554d-035e-4325-b0a4-d5ec938d44a7" />
<img width="2100" height="1200" alt="delivery_fee" src="https://github.com/user-attachments/assets/2efe6b3e-0f3f-47ac-b37f-13663861c1d7" />
<img width="2100" height="1200" alt="restaurant_quality" src="https://github.com/user-attachments/assets/999e78aa-2bbd-4eaa-85a5-39ab11c2e9bc" />


---

## How to Run

```bash
pip install -r requirements.txt

python src/generate_data.py

python src/run_funnel_analysis.py
```
