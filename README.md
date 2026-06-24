# Intern Git Practice Lab

This repository is used by summer internship students to practice a professional Git workflow in a small robot-development project.

## Purpose

The project provides a safe environment to practice working on a dedicated branch, making focused commits, reviewing changes, and preparing a Pull Request. The files represent common documentation and scripting tasks that may appear in an engineering internship.

## Project Structure

- `interns/interns.md` - internship participant information and interests.
- `robot/startup_checklist.md` - verification steps before starting the robot.
- `robot/safety_rules.md` - engineering safety rules for robot operation.
- `scripts/task_summary.py` - a simple task-summary script.
- `logs/daily_log.md` - a short daily work record.

## Working Guidelines

- Create and work on your own branch instead of `main`.
- Keep commits small, clear, and related to one task.
- Review changes with `git status` and `git diff` before committing.
- Do not commit temporary files, logs, build outputs, or secrets.

## Run the Task Summary

```bash
python3 scripts/task_summary.py
```
