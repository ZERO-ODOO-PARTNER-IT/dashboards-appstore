# Activities - Tutorial Guide

## Introduction

**Activities** is a comprehensive activity management dashboard for Odoo 18. It provides a centralized hub for tracking, managing, and analyzing all activities across your organization.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Quick Access Menu](#quick-access-menu)
3. [Managing Activities](#managing-activities)
4. [Reporting & Analytics](#reporting--analytics)
5. [Configuration](#configuration)
6. [Tips & Best Practices](#tips--best-practices)

---

## Getting Started

### Installation

1. Navigate to **Apps** in your Odoo instance
2. Search for "Activities"
3. Click **Install**
4. Once installed, the app will appear in your main menu

### First Launch

After installation, click on the **Activities** app icon in your main menu. You'll be greeted with the Quick Access view showing your assigned activities.

---

## Quick Access Menu

The **Quick Access** menu provides instant access to your most important activity views:

### My Activities
- Shows all activities assigned to you
- Default view when opening the app
- Displays activities in a Kanban board format

### Overdue
- Lists all activities past their deadline
- Highlighted in red for urgency
- Helps prioritize late follow-ups

### Today
- Shows activities due today
- Perfect for daily planning
- Displayed with orange indicators

---

## Managing Activities

### Available Views

OX Activity provides multiple ways to view your activities:

| View | Best For |
|------|----------|
| **List** | Quick scanning and bulk actions |
| **Kanban** | Visual workflow management |
| **Calendar** | Time-based planning |
| **Form** | Detailed activity information |
| **Pivot** | Data analysis |
| **Graph** | Visual reporting |

### Activity List View

The list view displays activities with the following information:
- **Activity Type** - Category of the activity (Call, Meeting, Email, etc.)
- **Summary** - Brief description of the activity
- **Document Model** - Related Odoo model
- **Document Name** - Linked record name
- **Assigned To** - Responsible user
- **Deadline** - Due date
- **Status** - Overdue, Today, or Planned

#### Color Coding
- 🔴 **Red** - Overdue activities
- 🟠 **Orange** - Due today
- 🟢 **Green** - Planned (future)

### Kanban View

Activities are grouped by **Activity Type** by default. Each card shows:
- Assigned user avatar
- Activity summary
- Related document
- Days remaining until deadline
- Status badge

### Calendar View

View activities on a monthly/weekly/daily calendar:
- Color-coded by activity type
- Drag-and-drop to reschedule
- Click to view details or edit

### Creating an Activity

1. Click the **Create** button
2. Fill in the required fields:
   - **Activity Type** - Select from available types
   - **Summary** - Brief description
   - **Assigned To** - Select a user
   - **Deadline** - Set the due date
3. Add optional notes in the **Notes** tab
4. Click **Save**

---

## Reporting & Analytics

The **Reporting** menu provides powerful analytics tools:

### Graph View

- Bar charts showing activities by type and user
- Visual representation of workload distribution
- Identify bottlenecks at a glance

### Pivot Table

- Cross-tabulate activities by multiple dimensions
- Analyze by user, type, status, and time period
- Export data to Excel/CSV for further analysis

### Available Filters

- **My Activities** - Filter to only your assignments
- **Overdue** - Show past-due items
- **Today** - Today's activities
- **Planned** - Future activities
- **This Week** - Current week
- **This Month** - Current month

### Grouping Options

Group activities by:
- Assigned User
- Activity Type
- Document Model
- Deadline (Day/Month)
- Status

---

## Configuration

### Activity Types

Access via **Configuration > Activity Types**

Activity types define the categories of activities available in your system:

| Field | Description |
|-------|-------------|
| **Name** | Display name of the activity type |
| **Category** | Default, Meeting, or Phone Call |
| **Icon** | Visual identifier |
| **Default User** | Auto-assigned user |
| **Delay** | Default deadline offset |
| **Decoration** | Color styling |

### Creating Custom Activity Types

1. Go to **Configuration > Activity Types**
2. Click **Create**
3. Configure the activity type:
   - Set a descriptive name
   - Choose the category
   - Define default scheduling (delay days)
   - Select an icon
4. Save the activity type

---

## Tips & Best Practices

### Daily Workflow

1. **Morning Review**
   - Check "Today" view for immediate priorities
   - Review "Overdue" for catch-up items

2. **Throughout the Day**
   - Mark activities as done when completed
   - Create follow-up activities as needed

3. **End of Day**
   - Review tomorrow's planned activities
   - Reschedule if necessary

### Team Management

- Use the **Reporting** view to monitor team workload
- Filter by user to check individual performance
- Identify overdue patterns to address bottlenecks

### Efficiency Tips

1. **Use Keyboard Shortcuts**
   - Press `Alt + Q` to quickly search
   - Use `Ctrl + K` for command palette

2. **Leverage Filters**
   - Save frequently used filter combinations
   - Create custom search presets

3. **Calendar Integration**
   - Sync with external calendars
   - Set reminders for important activities

### Status Meanings

| Status | Description |
|--------|-------------|
| **Planned** | Activity scheduled for the future |
| **Today** | Activity due today |
| **Overdue** | Activity past deadline |

---

## Security & Access Rights

### User Groups

| Group | Permissions |
|-------|-------------|
| **User** | View, create, edit, delete own activities |
| **Manager** | Full access + Activity Types configuration |

### Access Configuration

Managers can configure activity types and have full control over the module settings. Regular users can manage their own activities and view activities assigned to them.

---

## Support

For technical support or feature requests, please contact:

**The Odoo Experts**  
Website: https://www.theodooexperts.com

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 18.0.1.0.0 | 2026-02 | Initial release |

---

*© 2026 The Odoo Experts. All rights reserved.*
