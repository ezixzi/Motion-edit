# Reels production automation kit

Portable production inputs for the user's explicit request to produce three original AI/technology MP4s per execution and publish them to ezixzi/Motion-edit. The schedule belongs to the ChatGPT task; this repository is the durable source/template/queue, not a GitHub Actions cron.

## Inputs and first batch

Read SEED_SCRIPTS.md as source material/editorial guidance. Current direct user preference takes precedence: NO GENERATED NARRATION, NO MUSIC; user will dub independently. Timing/word-count targets in the attachment are guidance, not proof of real reading duration. No paid generation services, voice cloning or model downloads are required. Follow seed-queue.json and state.json, starting with the three seed topics. After they are used, research three relevant AI/technology stories, avoid repetitions, and verify primary sources and publication dates. Do not invent discoveries, precision or links. Bounded corrections for factual accuracy are authorized; record them in production notes.

Initial source audit (29 October 2026): all three source URLs were opened successfully with the web research tool. MIT microrobot article reports speed gain about450%, not an independently verified exact447%; use sekitar450% unless the paper supports447. Ten flips in11s is verified. Stanford:27/32 ONE-YEAR COMPLETERS could read,38 enrolled, advanced AMD/geographic atrophy, not restored normal vision or all blindness. Battery: special acoustic equipment records faint signals; not an audible warning feature available in ordinary phones. The source news dates and research limitations must appear in metadata/source notes.

## Visual contract

Use supplied male voxel avatar: brown short square hair, black glasses, navy circuit hoodie, lime/cyan shoes. Preserve identity. Full body, both feet visible. Articulated gestures, blink/head movement, and script-based mouth cues throughout; left/right placement follows visual subject. Do not claim actual audio lip sync when no narration exists.

1080×1920 9:16,30fps, roughly35–50seconds as natural editorial timing allows. Navy#061116/lime#b1ff52/cyan#37e5d0/off-white, Space Grotesk headings and Plus Jakarta Sans captions. Top highlight/object name enters as ONE animated masked/depth block and then stays stable. Lower narration captions at x75..940,y1365..1460 reveal words smoothly. Headings aroundy315..480. Active hostx0 or525,y900,size440 ends before1340. Safe guide:user's top220,bottom450,left35,rightbutton100; keep important text comfortable insidex75..940. Respect foreground host and avoid overlaps. Covers/platform UI can crop differently.

Make motion specific to the mechanism, not decorative floating cards: establishing shot→push toward mechanism→hold→wider return; purposeful pans, orbit-like object movement, parallax, drawn callouts, connected transitions. Use original 3D/conceptual diagrams rather than borrowed research imagery unless its license permits the intended use. Label conceptual/schematic reconstructions. Do not imply photoreal footage is a real experiment. Show meaningful topic-specific objects: microrobot wings/controller/flight, retina/glasses/IR signal, battery sensor/bubbles/fractures. **The included Codex example is a working layout reference, not the science videos. Do not simply replace its labels and deliver the same Codex panels for unrelated research topics.**

## Local execution

Existing full project may be available at /workspace/work/auction-film. This portable kit is /workspace/work/reels-automation-kit, mirrored at automation/reels in the repository. If local state is missing, fetch just this subtree through GitHub/API/raw URLs (avoid downloading all historical MP4s). Install pinned dependencies with npm install. Need Node,FFmpeg/FFprobe,Chromium. Set REELS_CHROMIUM to a supported browser path if autodetection fails. No credentials or secret files belong in this kit.

- `npm run check` validates TypeScript.
- `node scripts/sfx.mjs` regenerates sparse original SFX from public/script.json using Node and FFmpeg, without voice or music.
- `STILL_ONLY=1 node scripts/render.mjs ReelExample out/smoke.mp4` renders a frame60 preview.
- `node scripts/render.mjs ReelExample out/example.mp4` renders and fully decodes H264/AAC MP4.
- Add independently named compositions and matching JSON/SFX for each new topic; align durationInFrames with script data. Do not overwrite example or other outputs if user changes them.
- Caption JSON uses Caption schema:text,startMs,endMs,timestampMs:null,confidence:null. Generate local timestamped Indonesian dubbing script and SRT for each video.

Kit validation on setup:TypeScript passed, original SFX generation succeeded, Chromium preview frame rendered. Previous full workflow successfully rendered/decoded/uploaded multiple MP4s with remote SHA256 matches. This is not a guarantee every future environment is available.

## Batch transaction and publication

At start read remote state.json and existing outputs. Reserve a fresh timestamped batch in active_batch with started_at and intended topic IDs. Respect an active non-stale execution instead of running duplicate renders. After stale/interrupted runs reconcile already published outputs and resume uncompleted topics; do not blindly erase another run's state. Use expected GitHub head leases and preserve base tree on every commit. No force-push, no replacing old MP4s.

Write three distinct MP4s under outputs/ai-tech/YYYYMMDD-HHMMWIB-slug.mp4. Log each published video in state.completed with topic_id,title,source_urls,source_dates,output_path,sha256,published_at; remove from pending only after upload and remote verification. Include short source/correction/visual QA notes. Update state in the same Git tree as outputs where practical. Once all seeds are done, append newly researched topics to completed so later batches avoid them. Never mark failed or missing files complete.

QA:all three original topics supported, correct dates and quantities, clear hook, logical escalated facts and contextual ending; TypeScript passes; inspect several frames including zoom extrema/scene transitions; text not clipped/overlapping, avatar head/hands/feet intact, important content in safe guide; FFprobe correct dimensions/runtime/codecs, decode entire video, confirm SFX-only audio with no clipping; download immutable GitHub raw output and match SHA256. Deliver actual download links, titles, timecodes/scripts and source notes. Repository receives MP4s and minimal automation state/production records; do not publish credentials, unrelated private files or unsolicited workbench ZIPs. Do not post to social platforms or message others.

Use current tools/network policy; preserve proxy and TLS. The user's authorization permits requested research/render/GitHub publishing, but does not technically disable network restrictions. If a service requires Connect/Reconnect, stop for that connection; if runtime/network blocks completion, report the concrete blocker and partial results without claiming success. Don't turn the production task into a reminder or a script-only answer.
