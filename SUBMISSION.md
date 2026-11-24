# Submission — The Worst App Idea Ever Pitched

## Bounty facts

- Slug: `u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23`
- Title: The Worst App Idea Ever Pitched
- Page: https://make.fun/competitions/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23
- Prize: $2 total — top 8 (1st $0.64, 2nd $0.45, 3rd $0.31, 4th $0.22, 5th $0.15, 6th $0.11, 7th $0.07, 8th $0.05)
- Deadline: 2026-11-26T16:50:00Z (23:50 WIB)
- Repo name: `u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23`
- Kit: downloaded from https://make.fun/c/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/kit
- Kit sha256: `c36c93b8b2df64979fc52e9cc08fea9a8551c3b2a0cdf7ac1db6b2d4c3f2e59a`
- Kit bundle_sha256: `fbf6238335bafaa40b18d828a9ea90f71c7f091dc360de035aae2ace61aa47f7`

## Chosen line

> Pebble is the world's first app that lets you adopt, name, and emotionally support a single rock in your garden, with daily check-ins and a grief counselor for when it erodes.

- Characters: 175 (limit 240)
- Bytes (UTF-8): 175
- `entry.txt` sha256: `6cc41485b81aba9e464f38e41fc9805f4a0997c9a55022f6cc5e0c7dca2f0f5c`
- No trailing newline. Deterministic: two local runs produced byte-identical output.
- Gate check: 1–240 chars, UTF-8, not whitespace-only — passes.

## Why this line, over the other candidates

- **A (chosen):** "Pebble is the world's first app that lets you adopt, name, and emotionally support a single rock in your garden, with daily check-ins and a grief counselor for when it erodes."
  Deadpan founder voice: a named product, a specific useless function, and a problem
  nobody has — a rock that needs emotional support — solved with total confidence.
  The absurdity escalates inside the sentence itself (adopt → name → emotionally
  support → daily check-ins → grief counselor for erosion), and every clause leaves a
  vivid, specific picture. It never winks; the founder means every word, which is
  exactly what criteria 2 and 3 reward.
- **B:** "Napkin syncs your sneezes to the cloud, so your future self can relive every
  allergy season in stunning high definition." Funny image, but the app's function is
  vague — reliving sneezes is not a clear thing an app does — so it is weaker on
  criterion 1 (names a specific app and what it uselessly does).
- **C:** "Doorknob is a subscription app that texts you every morning to confirm your
  front door is still, in fact, a door." One-note gag; the "app" is barely an app and
  the picture is thinner than A's. Shorter, but it spends its characters on a single
  joke instead of building a product.
- **D:** "SockSync uses AI to match your socks by emotional compatibility, because a
  mismatched pair is the silent killer of modern productivity." Strong deadpan voice,
  but sock-pairing is a well-worn joke trope and the picture is less vivid and less
  specific than a named rock with a grief counselor.
- **E:** "Introducing Umbrella, the app that reminds you to bring an umbrella only after
  it has already started raining, using patented hindsight technology." "Patented
  hindsight technology" is a great line, but umbrella reminders are a real app
  category, so it reads as a buggy real app rather than a perfectly pointless one —
  weaker on criterion 1's "worst idea imaginable".

No line was crafted that beats A on criteria 1–2: A names the product and its useless
function in the first clause, the mismatch (a rock needing emotional support) is a
problem nobody has, and the sentence keeps escalating instead of explaining itself.

## Build status

- Built by subagent (build only — NO submit, NO GitHub mirror; parent does bundle/mirror/submit).
- Files: main.py, entry.txt, README.md (3 make.fun badges + bounty link), LICENSE (MIT),
  SUBMISSION.md, prompt-file.txt, kit.tar.gz, <slug>-kit/ (extracted kit).
- Bundle/check attempt: see "Bundle + check" section below.

## Bundle + check

- Bundle (builder attempt, diagnostic only — parent re-bundles with usage rows):
  `worst-app-bundle.tar.gz`, 113,728 bytes,
  sha256 `4c5845d1ca32db5d2ff6ea518cb7a7143e0775defe5f53ec6505bb03494a487b`
- Run record present: scheduled prompt ("saben ono bounty anyar langsung garap,
  pokok skip sing bayar"), system prompt uploaded, instruction files collected (1),
  MCP none.
- Check: **13 passed, 1 failed, 5 skipped, 5 at submission.**
  - FAIL: `thinking_priced` — 0 usage rows attached to the 1 Muse app session.
    Cause: a subagent's usage rows are written to muse.db only once its run
    completes, so the SELECT returned 0 rows mid-run. The parent (top-level agent
    faf6e1e3-2617-4888-b4a3-6edac215ad08) must pull usage rows for agent ids
    2976d8a6-fe9c-407a-ba8f-7315204cc998 (this builder) + its own, re-bundle with
    --muse-usage, and re-check. Nothing needs rebuilding.
  - Passed: competition_open, snapshot, license_osi, entrypoint,
    transcripts_present, transcripts_recorded, thinking_wellformed,
    thinking_in_window, thinking_reproduces (77.0% authored), thinking_turns,
    thinking_revised, transcripts_run_record, thinking_own_work.
  - At submission (resolve via mirror): repo_public, repo_owner,
    repo_created_after_open, commit_in_repo, duplicate_snapshot.
- NOT submitted (build only, per task). No GitHub mirror touched.
