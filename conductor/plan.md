# Master Implementation Plan: Plant Doctor (Django)

## Phase 1: Project Foundation
**Goal:** Initialize the Django project and set up the base infrastructure.

- [ ] **Initialize Django Project**
    - Create virtual environment.
    - Install `django` and `django-tailwind` (optional, or just use CDN as per prototype).
    - Start project `plantdoctor`.
- [ ] **App Structure**
    - Create apps: `core` (home, landing), `users` (auth), `diagnose` (scanner, results).
- [ ] **Static & Templates Setup**
    - Configure `STATICFILES_DIRS` and `TEMPLATES`.
    - Move Prototype HTML files to `templates/` folder (organized by app).
    - Move assets (images if any) to `static/` or keep CDN links.
    - Create a `base.html` template to share the common `<head>` and Tailwind config.

## Phase 2: Authentication & User Management
**Goal:** Allow users to sign up, log in, and manage their profiles.

- [ ] **User Model**
    - Extend `AbstractUser` in `users/models.py`.
    - Add fields: `full_name`, `location`, `avatar` (ImageField).
- [ ] **Auth Views**
    - Implement Login View (using `login.html`).
    - Implement Signup View (using `signup.html`).
    - Implement Logout.
- [ ] **Profile View**
    - Implement Profile management (using `profile.html`).
    - Allow updating name/location.
- [ ] **Onboarding**
    - specific view for `onboarding.html` shown after first signup.

## Phase 3: Core Logic (Scanner & Diagnosis)
**Goal:** Implement the scanning workflow and display results.

- [ ] **Data Models**
    - `Disease`: Name, Description, Immediate Action, Long Term Care, Recommended Products (JSON or related model).
    - `Scan`: ForeignKey to User, ImageField, Date, Result (ForeignKey to Disease), Confidence Score.
- [ ] **Scanner View**
    - Render `scanner.html`.
    - Handle file upload (mocking the camera capture if needed).
- [ ] **Analysis Logic**
    - **Integrate AI Vision API:** Use a multimodal AI (e.g., Gemini API, OpenAI Vision) to analyze uploaded plant images.
    - **Prompt Engineering:** Design a system prompt to instruct the AI to identify plant diseases and return structured JSON data (Disease Name, Confidence, Immediate Actions, Long-term Care).
    - **Handling:** Parse the AI response and save it to the `Scan` model.
- [ ] **Result View**
    - Render `result.html` with dynamic data from the `Scan` result.
    - Display the specific advice for the detected disease.

## Phase 4: Dashboard & History
**Goal:** Tie everything together in the user dashboard.

- [ ] **Dashboard View**
    - Render `dashboard.html`.
    - Fetch and display the user's `Scan` history (limit 5).
    - "My Garden" section: Show saved scans/plants.
- [ ] **History View**
    - Full list of past scans.
- [ ] **Navigation**
    - Ensure all links in the templates (Home, Login, Profile, Dashboard) point to the correct Django URLs.

## Phase 5: Refinement
**Goal:** Polish the UI and ensure smooth UX.

- [ ] **Template Inheritance**
    - Refactor all HTML files to extend `base.html` to reduce duplication.
- [ ] **Error Handling**
    - 404/500 pages.
    - Form validation errors display.
- [ ] **Admin Panel**
    - Configure Django Admin to easily add/edit `Disease` data.

## Phase 6: Final Review
- [ ] Verify flow: Landing -> Signup -> Onboarding -> Dashboard -> Scan -> Result.
- [ ] Check responsiveness (Mobile/Desktop).
