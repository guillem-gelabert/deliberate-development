---
title: "Twenty Ways to Split Stories"
author: Bill Wake
url: https://xp123.com/twenty-ways-to-split-stories/
retrieved_at: 2026-09-25
published_at: "2005-09 (XP Day talk; revised 2006-01-06, 2006-07-19, 2011-01-08)"
source_type: blog article
normalization_notes: "Splitting tables rebuilt from HTML (pandoc could not convert nested layout); the linked PDF summary sheet was not fetched."
---

# Twenty Ways to Split Stories

> The ability to split stories is an important skill for customers and developers on XP teams. This note suggests a number of dimensions along which you might divide your stories. (Added July, 2009: summary sheet (PDF), French translation (PDF).)

Splitting stories lets us separate the parts that are of high value from those of low value, so we can spend our time on the valuable parts of a feature. (Occasionally, we have to go the other way as well, combining stories so they become big enough to be interesting.) There’s usually a lot of value in getting a minimal, end-to-end solution present, then filling in the rest of the solution. These “splits” are intended to help you do that.

## The splits

### The Big Picture

| Easier | Harder | Why |
|---|---|---|
| Research | Action | It’s easier to research how to do something than to do it (where the latter has to include whatever research is needed to get the job done). So, if a story is too hard, one split is to spend some time researching solutions to it. |
| Spike | Implementation | Developers may not have a good feeling for how to do something, or for the key dimensions on which you might split a story. You can buy learning for the price of a spike (a focused, hands-on experiment on some aspect of the system). A spike might last an hour, or a day, rarely longer. |
| Manual | Automated | If there’s a manual process in place, it’s easier to just use that. (It may not be better but it’s less automation work.) For example, a sales system required a credit check. The initial implementation funneled such requests to a group that did the work manually. This let the system be released earlier; the automated credit check system was developed later. And it was not really throw-away work either – there was always going to be a manual process for borderline scores. |
| Buy | Build | Sometimes, what you want already exists, and you can just buy it. For example, you might find a custom widget that costs a few hundred dollars. It might cost you many times that to develop yourself. |
| Build | Buy | Other times, the “off-the-shelf” solution is a poor match for your reality, and the time you spent customizing it might have been better spent developing your own solution. |

### User Experience

| Easier | Harder | Why |
|---|---|---|
| Batch | Online | A batch system doesn’t have to interact directly with the user. |
| Single-User | Multi-User | You don’t face issues of “what happens when two users try to do the same thing at the same time.” You also may not have to worry about user accounts and keeping track of the users. |
| API only | User Interface | It’s easier to not have a user interface at all. For example, if you’re testing your ability to connect to another system, the first cut might settle for a unit test calling the connection objects. |
| Character UI or Script UI | GUI | A simple interface can suffice to prove out critical areas. |
| Generic UI | Custom UI | At one level, you can use basic widgets before you get fancy with their styles. To go even further, something like Naked Objects infers a default user interface from a set of objects. (The Naked Objects project has split into Naked Objects for .Net and Apache Isis for Java) |

### “Ilities”

| Easier | Harder | Why |
|---|---|---|
| Static | Dynamic | It’s easier to calculate something once than ensure it has the correct value every time its antecedents change. Sometimes, you can use a halfway approach: periodically check for a needed update, but don’t do it until the user requests it. |
| Ignore errors | Handle errors | While it’s less work to ignore errors, that doesn’t mean you should swallow exceptions. Rather, the recovery code can be minimized. |
| Transient | Persistent | Let’s you get the objects right without the worries about changing the mapping of persisted data. |
| Low fidelity | High fidelity | You can break some features down by quality of result. E.g., a digital camera could start as a 1-pixel black-and-white camera, then improve along several axes: 9 pixels, 256 pixels, 10,000 pixels; 3-bit color, 12-bit color, 24-bit color; 75% color accuracy, 90% color accuracy, 95% color accuracy.” (William Pietri) |
| Unreliable | Reliable | “Perfect uptime is very expensive. Approach it incrementally, measuring as you go.” (William Pietri) |
| Small scale | Large scale | “A system that works for a few people for moderate data sets is a given. After that, each step is a new story. Don’t forget the load tests!” (William Pietri) |
| Less “ilities,” e.g., slower | More “ilities” | It’s easier to defer non-functional requirements. (A common strategy is to set up spikes as side projects to prove out architectural strategies.) |

### Features

| Easier | Harder | Why |
|---|---|---|
| Few features | Many features | Fewer is easier. |
| Main flow | Alternate flows | (Use case terminology.) The main flow – the basic happy path – is usually the one with the most value. (If you can’t complete the most trivial transaction, who cares that you have great recovery if step 3 goes bad?) |
| 0 | 1 | Hardware architects have a “0, 1, infinity” rule – these are the easiest three values to handle. Special cases bring in issues of resource management. |
| 1 | Many | It’s usually easiest to get one right and then move to a collection. |
| Split condition | Full condition | Treat “and,” “or,” and “then” and other connector words as opportunities to split. Simplify a condition, or do only one part of a multi-step sequence. |
| One level | All levels | One level is the base case for a multi-level problem. |
| Base case | General case | In general, you have to do a base case first (to have any assurance that recursive solutions will terminate). |

## Summary

These “splits” may help give you ideas when you’re looking for a way to move forward in small steps. While it’s important to be able to split stories, don’t forget that you have to reassemble them to get the full functionality. But you’ll usually find that there is a narrow but high-value path through your system.

\[Developed for XP Day speech, Sept., 2005. January 6, 2006: Thanks to William Pietri for sharing his suggestions on the fidelity, reliability, and scale dimensions. Fixed typo, 7-19-06. Added “connectors”, 1-8-11.\]
