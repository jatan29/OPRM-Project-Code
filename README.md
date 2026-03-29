# Airline Revenue Management Optimization: Case Study Flight AI2401

## 📌 Project Overview
[cite_start]This repository contains the quantitative models, data tracking scripts, and interactive visualization tools designed to optimize pricing and revenue mechanisms in the airline industry[cite: 1, 2]. [cite_start]Built as an academic Operations Management project, the case study focuses on Flight AI2401 (Mumbai to Bangalore), operating an Airbus A320 Neo with a physical capacity of 164 seats[cite: 3, 5, 7]. 

[cite_start]The primary objective is to maximize expected flight revenue under demand uncertainty by tackling two structural challenges: perishable inventory and high fixed costs[cite: 11].

## 🚀 Key Features & Repository Structure

* **`flight_tracker.py` (Live Data Collection):** A Python backend script that integrates with the Amadeus API to fetch real-time flight offers. It parses pricing data for specific routes and automatically logs the daily fare trajectories into a Google Sheet.
* **`AI2401_RM_Dashboard.html` (Interactive Dashboard):** A frontend visualization tool built with HTML, CSS, and Chart.js. It allows users to simulate demand parameters and view real-time calculations for:
    * Dynamic Price Trajectories
    * EMSR-b (Expected Marginal Seat Revenue) Allocations
    * Overbooking Sensitivities
    * Overall Revenue Simulations 
* **`GROUP9OPRM.pdf` (Project Presentation):** The comprehensive slide deck detailing the mathematical framework, logic bridges, and strategic implications of the applied revenue management policies.

## 🧮 Mathematical Framework

[cite_start]The project utilizes two distinct strategic levers to dictate final flight revenue[cite: 18]:

### 1. Capacity Allocation (EMSR)
[cite_start]To prevent rejecting early low-fare demand only for high-fare demand to fail to materialize (spoilage), we utilize the Expected Marginal Seat Revenue (EMSR) protection rule[cite: 19, 78, 79]. 
* **Critical Ratio:** $P(D_{H} \le y) = \frac{f_{H} - f_{L}}{f_{H}}$ [cite: 111]
* [cite_start]**Result:** Precisely 48 seats must be protected (fenced) for high-fare passengers[cite: 129].

### 2. Overbooking (Newsvendor Model)
[cite_start]To hedge against no-shows and ensure maximum physical utilization, we balance the underage cost (empty seats) against the overage cost (denied boarding compensation)[cite: 11, 74].
* **Critical Ratio:** $P(s \ge C) = \frac{p}{D}$ [cite: 92, 93]
* [cite_start]**Result:** The optimal booking limit is 180 tickets for a 164-seat physical cabin[cite: 128]. [cite_start]Selling 16 seats beyond physical capacity mathematically minimizes revenue lost from no-shows[cite: 104].

## 📊 Strategic Outcomes
[cite_start]Deploying these combined Revenue Management policies reliably lifts total flight revenue by 5-10% compared to a standard first-come, first-served model[cite: 133]. [cite_start]It transforms raw capacity into optimized yield, driving pure margin improvement[cite: 147].

## 🛠️ Setup & Installation

### Python Flight Tracker
1. Ensure you have Python installed along with the required libraries (`requests`, `gspread`, `google-auth`).
2. Obtain your Amadeus API keys and place them in the script.
3. Configure your Google Cloud service account and place the `credentials.json` file in the root directory.
4. Run `python flight_tracker.py` to fetch and log the latest prices.

### Interactive Dashboard
1. Simply download `AI2401_RM_Dashboard.html` and open it in any modern web browser. No local server is required. 

## 👥 Contributors (Group 9)
* [cite_start]Jatan Mukesh (2410206) [cite: 9]
* Sohan Kulkarni (2410243) [cite: 9]
* [cite_start]Aniruddha Wankhade (2410345) [cite: 9]
* [cite_start]Pratik Nagpure (2410301) [cite: 9]
* Yash Pise (2410307) [cite: 9]
* [cite_start]Shonraj Patil (2410326) [cite: 9]
