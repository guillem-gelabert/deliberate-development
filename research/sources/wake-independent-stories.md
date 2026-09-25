---
title: "Independent Stories in the INVEST Model"
author: Bill Wake
url: https://xp123.com/independent-stories-in-the-invest-model/
retrieved_at: 2026-09-25
published_at: "unknown (not shown on page)"
source_type: blog article
normalization_notes: "Removed translation link; marked pull quotes (in-page callouts) as blockquotes."
---

# Independent Stories in the INVEST Model

The [INVEST](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/) model is a reminder of the important characteristics of user stories, and it starts with **I** for **Independent**.

Independent stories each describe different aspects of a system’s capabilities. They are easier to work with because each one can be (mostly) understood, tracked, implemented, tested, etc. on its own.

Agile software approaches are flexible, better able to pursue whatever *is* most valuable today, not constrained to follow a 6-month old guess about what *would be* most valuable today. Independent stories help make that true: rather than a “take it or leave it” lump, they let us focus on particular aspects of a system.

We would like a system’s description to be consistent and complete. Independent stories help with that too: by avoiding overlap, they reduce places where descriptions contradict each other, and they make it easier to consider whether we’ve described everything we need.

> *Pull quote:* Three common types of dependency: overlap, order, and containment

What makes stories dependent rather than independent? There are three common types of dependency: *overlap* (undesirable), *order* (mostly can be worked around), and *containment* (sometimes helpful).

## Overlap Dependency

Overlap is the most painful form of dependency. Imagine a set of underlying capabilities:\
{A, B, C, D, E, F}\
with stories that cover various subsets:\
{A, B}\
{A, B, F}\
{B, C, D}\
{B, C, F}\
{B, E}\
{E, F}

Quick: what’s the smallest set of stories that ensure that capabilities {A, B, C, D, E, F} are present? What about {A, B, C, E}? Can we get those and nothing else?

When stories overlap, it’s hard to ensure that everything is covered at least once, and we risk confusion when things are covered more than once.

> *Pull quote:* Overlapping stories create confusion.

For example, consider an email system with the stories “User sends and receives messages” and “User sends and replies to messages.” (Just seeing the word “and” in a story title can make you suspicious, but you really have to consider multiple stories to know if there’s overlap.) Both stories mention sending a message. We can partition the stories differently to reduce overlap:

User sends \[new\] message\
User receives message\
User replies to message

(Note that we’re not concerned about “technical” overlap at this level: sending and replying to messages would presumably share a lot of technical tasks. How we design the system or schedule the work is not our primary concern when we’re trying to understand the system’s behavior.)

## Order Dependency

A second common dependency is order dependency: “this story must be implemented before that one.”

> *Pull quote:* Order dependencies complicate a plan, but we can usually eliminate them.

While there’s no approach that guarantees it, order dependency tends to be something that is mostly harmless and can be worked around. There are several reasons for that:

1.  Some order dependencies flow from the nature of the problem. For example, a story “User re-sends a message” naturally follows “User sends message.” Even if there is an order dependency we can’t eliminate, it doesn’t matter since the business will tend to schedule these stories in a way that reflects it.
2.  Even when a dependency exists, there’s only a 50/50 chance we’ll want to schedule things in the “wrong” order.
3.  We can find clever ways to remove most of the order dependencies.

For example, a user might need an account before they can send email. That might make us think we need to implement the account management stories first (stories like “Admin creates account”). Instead, we could build in (“hard-code”) the initial accounts. (You might look at this as “hard-coding” or you might think of it as “the skinniest possible version of account management”; either way, it’s a lot less work.)

Why take that approach? Because we want to explore certain areas first. We consider both value and risk. On the value side, we may focus on the parts paying customers will value most (to attract them with an early delivery). On the risk side, we may find it important to address risks, thinking of them as negative value.  In our example, we may be concerned about poor usability as a risk. A few hard-coded accounts would be enough to let us explore the usability concerns.

## Containment Dependency

Containment dependency comes in when we organize stories hierarchically: “this story contains these others.” Teams use different terms for this idea: you might hear talk of “themes, epics, and stories,” “features and stories,” “stories and sub-stories,” etc. A hierarchy is an organizational tool; it can be used formally or informally.

> *Pull quote:* A good organization for *describing* a system is rarely the best organization for *scheduling* its implementation.

The biggest caveat about a hierarchical decomposition is that while it’s a helpful strategy for organizing and understanding a large set of stories, it doesn’t make a good scheduling strategy. It can encourage you to do a “depth-first” schedule: address this area, and when it’s done, go the next area. But really, it’s unlikely that the most valuable stories will all be in a single area. Rather, we benefit from first creating a minimal version of the whole system, then a fancier version (with the next most important feature), and so on.

## Bottom Line

Independent stories help both the business and technical sides of a project. From a business perspective, the project gets a simple model focused on the business goals, not over-constrained by technical dependencies. From a technical perspective, independent stories encourage a minimal implementation, and support design approaches that minimize and mange implementation dependencies.

### Related Material

- “[INVEST in Good Stories, and SMART Tasks](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)” – the original article describing the INVEST model
- [**N**egotiable Stories in the INVEST Model](http://xp123.com/articles/negotiable-stories-in-the-invest-model/)
- [**V**aluable Stories in the INVEST Model](http://xp123.com/articles/valuable-stories-in-the-invest-model/)
- [**E**stimable Stories in the INVEST Model](http://xp123.com/articles/estimable-stories-in-the-invest-model/)
- [**S**mall – Scalable – Stories in the INVEST Model](http://xp123.com/articles/small-scalable-stories-in-the-invest-model/)
- [**T**estable Stories in the INVEST Model](https://xp123.com/articles/testable-stories-in-the-invest-model/)
- *[Composing User Stories](https://elearning.industriallogic.com/gh/submit?Action=AlbumContentsAction&album=composingUserStories&devLanguage=None)* – eLearning from Industrial Logic
- [*User Stories Applied*](http://www.amazon.com/exec/obidos/ASIN/0321205685/xp123com), by Mike Cohn
