# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
The rules for this file:
  * entries are sorted newest-first.
  * summarize sets of changes - don't reproduce every git log comment here.
  * don't ever delete anything.
  * keep the format consistent:
    * do not use tabs but use spaces for formatting
    * 79 char width
    * YYYY-MM-DD date format (following ISO 8601)
  * accompany each entry with github issue/PR number (Issue #xyz)
-->

## [Unreleased]

### Authors

### Added
<!-- Added functionality -->

### Fixed
<!-- Fixes -->

### Changed
<!-- Changes in existing functionality -->

### Deprecated
<!-- Soon-to-be removed features -->

### Removed
<!-- Removed features -->

## [1.0.0] - 2023-11-09

### Authors
- IAlibay
- lilyminium
- orbeckst
- ianmkenney

### Added
- wheel deployment workflow (#22)

### Fixed
- documentation fixes (#13, #18, #49, #51)

### Changed
- switched from versioneer to versioningit (#53)

## [0.1.0] - 2023-08-25

The original `MDAnalysis.analysis.encore` was written by Matteo Tiberti,
Wouter Boomsma, and Tone Bengtsen in 2016 and had been part of MDAnalysis
since release 0.16.0,
https://docs.mdanalysis.org/2.6.1/documentation_pages/analysis/encore.html.
Ian Kenney created the `mdaencore` MDAKit in 2023, based on the original code
in MDAnalysis. Additional contributors to the original source code are listed
in the AUTHORS.md file.

### Authors
- ianmkenney

### Added
- the core functionality of mdaencore (and its tests) was implemented
  using the source code from MDAnalysis.analysis.encore
- documentation deployed to github pages and read the docs (#1)

### Fixed
- removed ffast-math compiler flag (PR #14)


[Unreleased]: https://github.com/MDAnalysis/mdaencore/compare/1.0.0...HEAD
[1.0.0]: https://github.com/MDAnalysis/mdaencore/compare/0.1.0...1.0.0
[0.1.0]: https://github.com/MDAnalysis/mdaencore/releases/tag/0.1.0