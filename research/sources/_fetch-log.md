# Fetch log

Retrieved 2026-09-25 with `curl -L` (browser User-Agent, no auth, no bypass), main content isolated with BeautifulSoup, converted with pandoc (`gfm`), then hand-normalized (see `normalization_notes` in each file's frontmatter).

| Source | URL | HTTP | Result | File |
|---|---|---|---|---|
| Fowler — Specification By Example | https://martinfowler.com/bliki/SpecificationByExample.html | 200 | OK | fowler-specification-by-example.md |
| Fowler — Given When Then | https://martinfowler.com/bliki/GivenWhenThen.html | 200 | OK | fowler-given-when-then.md |
| Wake — INVEST in Good Stories, and SMART Tasks | https://xp123.com/invest-in-good-stories-and-smart-tasks/ | 200 | OK | wake-invest.md |
| Wake — Independent Stories in the INVEST Model | https://xp123.com/independent-stories-in-the-invest-model/ | 200 | OK | wake-independent-stories.md |
| Wake — Twenty Ways to Split Stories | https://xp123.com/twenty-ways-to-split-stories/ | 200 | OK (tables rebuilt; linked PDF not fetched) | wake-twenty-ways-to-split.md |
| Singer — Principles of Shaping | https://basecamp.com/shapeup/1.1-chapter-02 | 200 | OK | singer-principles-of-shaping.md |
| Singer — Set Boundaries | https://basecamp.com/shapeup/1.2-chapter-03 | 200 | OK | singer-set-boundaries.md |
| Singer — Risks and Rabbit Holes | https://basecamp.com/shapeup/1.4-chapter-05 | 200 | OK | singer-risks-and-rabbit-holes.md |
| Shape Up — book index (optional) | https://basecamp.com/shapeup | 200 | OK — landing page only (title, cover, TOC links); no content saved | — |
| Singer — Hand Over Responsibility (optional, ch. 10) | https://basecamp.com/shapeup/3.1-chapter-10 | 200 | OK — added: "Getting oriented", "Imagined vs discovered tasks" ground ORIENT | singer-hand-over-responsibility.md |
| Singer — Get One Piece Done (optional, ch. 11) | https://basecamp.com/shapeup/3.2-chapter-11 | 200 | OK — added: vertical slice, start in the middle (core/small/novel) | singer-get-one-piece-done.md |
| Singer — Show Progress (optional, ch. 13) | https://basecamp.com/shapeup/3.4-chapter-13 | 200 | OK — added: hill (uphill/downhill), estimates don't show uncertainty, sequencing | singer-show-progress.md |
| Singer — Decide When to Stop (optional, ch. 14) | https://basecamp.com/shapeup/3.5-chapter-14 | 200 | OK — added: baseline, scope hammering, when to extend | singer-decide-when-to-stop.md |
| Spolsky — Evidence Based Scheduling | https://www.joelonsoftware.com/2007/10/26/evidence-based-scheduling/ | 200 | OK | spolsky-evidence-based-scheduling.md |
| Newport — Focus Week: Take Control of Your Time | https://calnewport.com/focus-week-take-control-of-your-time/ | 200 | OK | newport-focus-week-time-blocking.md |
| Newport — Time-Block Planner | https://www.timeblockplanner.com/ | 200 | OK — product page; one method paragraph | newport-time-block-planner.md |
| Beck — Canon TDD | https://newsletter.kentbeck.com/p/canon-tdd | 200 | OK (public, not paywalled) | beck-canon-tdd.md |
| Fowler — Test Driven Development | https://martinfowler.com/bliki/TestDrivenDevelopment.html | 200 | OK | fowler-tdd.md |

Failures: none.
