# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).


## [0.5.7] - 2022-08-22

### Changed

- Release LAI docs as stable ([#14250](https://github.com/Lightning-AI/lightning/pull/14250))
- Compatibility for Python 3.10

### Fixed

- Pinning starsessions to 1.x ([#14333](https://github.com/Lightning-AI/lightning/pull/14333))
- Parsed local package versions ([#13933](https://github.com/Lightning-AI/lightning/pull/13933))


## [0.5.6] - 2022-08-16

### Fixed

- Resolved a bug where the `install` command was not installing the latest version of an app/component by default ([#14181](https://github.com/Lightning-AI/lightning/pull/14181))


## [0.5.5] - 2022-08-09

### Deprecated

- Deprecate sheety API ([#14004](https://github.com/Lightning-AI/lightning/pull/14004))

### Fixed

- Resolved a bug where the work statuses will grow quickly and be duplicated ([#13970](https://github.com/Lightning-AI/lightning/pull/13970))
- Resolved a bug about a race condition when sending the work state through the caller_queue ([#14074](https://github.com/Lightning-AI/lightning/pull/14074))
- Fixed Start Lightning App on Cloud if Repo Begins With Name "Lightning" ([#14025](https://github.com/Lightning-AI/lightning/pull/14025))


## [0.5.4] - 2022-08-01

### Changed

- Wrapped imports for traceability ([#13924](https://github.com/Lightning-AI/lightning/pull/13924))
- Set version as today ([#13906](https://github.com/Lightning-AI/lightning/pull/13906))

### Fixed

- Included app templates to the lightning and app packages ([#13731](https://github.com/Lightning-AI/lightning/pull/13731))
- Added UI for install all ([#13732](https://github.com/Lightning-AI/lightning/pull/13732))
- Fixed build meta pkg flow ([#13926](https://github.com/Lightning-AI/lightning/pull/13926))

## [0.5.3] - 2022-07-25

### Changed

- Pruned requirements duplicity ([#13739](https://github.com/Lightning-AI/lightning/pull/13739))

### Fixed

- Use correct python version in lightning component template ([#13790](https://github.com/Lightning-AI/lightning/pull/13790))

## [0.5.2] - 2022-07-18

### Added

- Update the Lightning App docs ([#13537](https://github.com/Lightning-AI/lightning/pull/13537))

### Changed

- Added `LIGHTNING_` prefix to Platform AWS credentials ([#13703](https://github.com/Lightning-AI/lightning/pull/13703))
