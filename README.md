# Airline Revenue Management Optimisation: Case Study Flight AI2401

## 📌 Project Overview
This repository contains the quantitative models, data tracking scripts, and interactive visualization tools designed to optimize pricing and revenue mechanisms in the airline industry. Built as an academic Operations Management project, the case study focuses on Flight AI2401 (Mumbai to Bangalore), operating an Airbus A320 Neo with a physical capacity of 164 seats. 

The primary objective is to maximise expected flight revenue under demand uncertainty by tackling two structural challenges: perishable inventory and high fixed costs.

## 🚀 Key Features & Repository Structure

* **`flight_tracker.py` (Live Data Collection):** A Python backend script that integrates with the Amadeus API to fetch real-time flight offers. It parses pricing data for specific routes and automatically logs the daily fare trajectories into a Google Sheet.
* **`AI2401_RM_Dashboard.html` (Interactive Dashboard):** A frontend visualisation tool built with HTML, CSS, and Chart.js. It allows users to simulate demand parameters and view real-time calculations for:
    * Dynamic Price Trajectories
    * EMSR-b (Expected Marginal Seat Revenue) Allocations
    * Overbooking Sensitivities
    * Overall Revenue Simulations 
* **`GROUP9OPRM.pdf` (Project Presentation):** The comprehensive slide deck detailing the mathematical framework, logic bridges, and strategic implications of the applied revenue management policies.

## 🧮 Mathematical Framework

The project utilises two distinct strategic levers to dictate final flight revenue[cite: 18]:

### 1. Capacity Allocation (EMSR)
To prevent rejecting early low-fare demand only for high-fare demand to fail to materialise (spoilage), we utilise the Expected Marginal Seat Revenue (EMSR) protection rule. 
* **Critical Ratio:** $P(D_{H} \le y) = \frac{f_{H} - f_{L}}{f_{H}}$
* **Result:** Precisely 48 seats must be protected (fenced) for high-fare passengers.

### 2. Overbooking (Newsvendor Model)
To hedge against no-shows and ensure maximum physical utilisation, we balance the underage cost (empty seats) against the overage cost (denied boarding compensation).
* **Critical Ratio:** $P(s \ge C) = \frac{p}{D}$
* [cite_start]**Result:** The optimal booking limit is 180 tickets for a 164-seat physical cabin[cite: 128]. [cite_start]Selling 16 seats beyond physical capacity mathematically minimises revenue lost from no-shows.

## 📊 Strategic Outcomes
Deploying these combined Revenue Management policies reliably lifts total flight revenue by 5-10% compared to a standard first-come, first-served model.It transforms raw capacity into optimised yield, driving pure margin improvement.

## 🛠️ Setup & Installation

### Python Flight Tracker
1. Ensure you have Python installed along with the required libraries (`requests`, `gspread`, `google-auth`).
2. Obtain your Amadeus API keys and place them in the script.
3. Configure your Google Cloud service account and place the `credentials.json` file in the root directory.
4. Run `python flight_tracker.py` to fetch and log the latest prices.

### Interactive Dashboard
1. Simply download `AI2401_RM_Dashboard.html` and open it in any modern web browser. No local server is required. 

## 👥 Contributors (Group 9)
* Jatan Mukesh (2410206)
* Sohan Kulkarni (2410243)
* Aniruddha Wankhade (2410345)
* Pratik Nagpure (2410301)
* Yash Pise (2410307)
* Shonraj Patil (2410326)
