# What you need to do for the group assignment (3 students / team)

Access the invitation link

Log in to GitHub (with your personal account).

Form teams of 3 students:

- The first one to enter → creates the team (e.g. team_01);
- The other two → join the already created team.

Once the team has 3 members, GitHub automatically creates the team repo.

## 🔧 **Scenario: Git Workflow for "Campus Events App"**

**Objective:** Demonstrate how a small student team collaborates using Git - from creating a feature branch to merging it back with a clean history.

### 🧩 Team Setup

- Repository: <https://github.com/cti-uoradea/campus-events-team01>
- Branching model: _trunk-based development_ (short-lived feature branches)
- Team members:
  - **Alex** - Frontend (React UI)
  - **Ioana** - Backend (API)
  - **Dan** - Testing & CI/CD

### 📜 Step-by-Step Story

#### 1️⃣ Initial Commit - Project Skeleton (from starter code)

main branch contains:

📦 campus-events/

┗ README.md

Command:

bash

git init

git add .

git commit -m "Initial project structure for Campus Events App"

Visual flow:

(main) o───● Initial project structure

#### 2️⃣ Create Feature Branch: "View Events List"

Alex creates a branch:

bash

git checkout -b feature/view-events

He edits **frontend/src/pages/EventsList.jsx**:

jsx

import React, { useEffect, useState } from "react";

export default function EventsList() {

const \[events, setEvents\] = useState(\[\]);

useEffect(() => {

fetch("<http://localhost:5000/api/events>")

.then(res => res.json())

.then(data => setEvents(data))

.catch(() => setEvents(\[\]));

}, \[\]);

return (

&lt;div&gt;

&lt;h2&gt;Upcoming Campus Events&lt;/h2&gt;

{events.length === 0 ? (

&lt;p&gt;No events available.&lt;/p&gt;

) : (

&lt;ul&gt;

{events.map(ev => (

&lt;li key={ev.id}&gt;

&lt;strong&gt;{ev.title}&lt;/strong&gt; - {ev.date}

&lt;/li&gt;

))}

&lt;/ul&gt;

)}

&lt;/div&gt;

);

}

Then commits:

bash

git add .

git commit -m "Add EventsList component with dummy data"

Visual flow:

(main) o───●───o

\\

(feature/view-events) ● Add EventsList component

#### 3️⃣ Ioana Adds Backend API on Another Branch

Ioana creates:

bash

git checkout -b feature/api-events

Creates backend logic by editing **backend/app.py**:

python

from flask import Flask, jsonify

app = Flask(\__name_\_)

\# Dummy event data

EVENTS = \[

{"id": 1, "title": "Hackathon 2025", "date": "2025-11-15"},

{"id": 2, "title": "AI Workshop", "date": "2025-12-01"},

\]

def create_app():

app = Flask(\__name_\_)

@app.route("/api/events")

def get_events():

return jsonify(EVENTS)

return app

\# Optional: allow local dev \`python backend/app.py\`

if \__name__ == "\__main_\_":

app = create_app()

app.run(debug=True)

Commits backend logic:

bash

git add .

git commit -m "Implement /api/events endpoint returning mock data"

Visual flow:

(main)

├── (feature/view-events) ●

└── (feature/api-events) ●

#### 4️⃣ Dan Configures CI

Dan works directly on a short branch:

bash

git checkout -b ci-setup

Adds GitHub Actions YAML in **.github/workflows/ci.yml**:

yaml

name: Campus Events CI

on:

push:

pull_request:

jobs:

build:

runs-on: ubuntu-latest

steps:

\- uses: actions/checkout@v4

\- name: Set up Python

uses: actions/setup-python@v5

with:

python-version: "3.11"

\- name: Install dependencies

run: |

python -m pip install --upgrade pip

pip install flask pytest requests

\- name: Run tests

run: pytest -v

When you push the branch, this job will be executed automatically. For the moment we don't have any tests.

Commits CI setup:

bash

git add .github/workflows/ci.yml

git commit -m "Add CI workflow for build and test"

Also adds a simple test script in **tests/****test_events.py**:

python

import sys

from pathlib import Path

\# make "backend" importable when running from repo root

sys.path.append(str(Path(\__file_\_).resolve().parents\[1\] / "backend"))

from app import create_app # noqa: E402

def test_events_endpoint_returns_list():

app = create_app()

client = app.test_client()

resp = client.get("/api/events")

assert resp.status_code == 200

data = resp.get_json()

assert isinstance(data, list)

assert len(data) >= 1

assert {"id", "title", "date"}.issubset(data\[0\].keys())

Then he commits this test:

bash

git add .

git commit -m "Add test for /api/events endpoint"

Then pushes all:

bash

git push origin ci-setup

#### 5️⃣ Open Pull Requests (PRs)

Each team member now opens a **Pull Request**:

- feature/view-events → _Add EventsList component_
- feature/api-events → _Implement API for events_
- ci-setup → _Add CI pipeline_

Each PR triggers CI and one peer review.

#### 6️⃣ Merge Flow & History

After approval:

bash

git checkout main

git merge --no-ff feature/view-events -m "Merge feature/view-events"

git merge --no-ff feature/api-events -m "Merge feature/api-events"

git merge --no-ff ci-setup -m "Merge CI setup"

Visual flow diagram:

(main)

o──● Initial structure

│

├───● Merge feature/view-events

│

├───● Merge feature/api-events

│

└───● Merge CI setup
