"""Build the proposed Chapter 1 storyboard package from approved locked story state."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / ".manga-studio"
STORYBOARD = WORK / "storyboard"
STORY = ROOT / "manga/03-story/arc-01/chapter-001"
PID = "ms-70391ae1065048cf8bdd564959abd6c3"
CHAPTER_ID = "chapter-fb585a7fd3e7450e936edbcfce992566"
ARCHIVE_SCENE = "scene-2f59e856c58d4d6db58d635cbc64e0bb"
STATION_SCENE = "scene-3b27382ec9a049e2acde70d7cf88fc10"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, value) -> None:
    write(path, json.dumps(value, indent=2))


# number, lines, scene, intent, pacing, purpose, reader effect, emotional curve,
# page-turn kind, page-turn setup, layout note, continuity handoff, panel rows
PAGES = [
    (1, "11-17", ARCHIVE_SCENE, "cinematic", "steady",
     "Establish Daniel's evidence-first worldview before the mystery enters.",
     "Trust Daniel's eye for material evidence and feel his isolation.", "1 -> 2", "question",
     "Why has San Aurelio Junction begun to bother him?",
     "Open with one dominant portrait-and-paper field, then three restrained evidence details.",
     "Daniel is in the municipal archive and has not yet visited the station.",
     [("Daniel studies paper under an archive lamp.", "Narration", "2 / 4", "Daniel Soriano trusted paper more than people."),
      ("A false date leaves a hard impression in a receipt.", "Evidence detail", "1 / 3", "Paper lied less often. When it did lie, it left evidence."),
      ("Old glue and an overwritten signature expose handling.", "Evidence detail", "1 / 3", "None"),
      ("Daniel looks toward the San Aurelio material.", "Emotional turn", "2 / 4", "That was why San Aurelio Junction had begun to bother him.")]),
    (2, "19-27", ARCHIVE_SCENE, "montage", "compressed",
     "Turn the archive intake into a deliberate pattern of omission.",
     "Move from institutional scale to the intimate violence of a removed name.", "2 -> 4", "reveal",
     "End on the missing-name strip.",
     "Use a broad intake panel with small overlapping evidence insets; keep the final clipped strip unobstructed.",
     "Forty-two boxes, three trunks, and the locked cash drawer remain distinct archive items.",
     [("Water-stained boxes, tin trunks, and the locked cash drawer fill intake tables.", "Establishing", "2 / 4", "Forty-two water-stained boxes. Three tin trunks. One locked station cash drawer."),
      ("Maribel assigns Daniel the first inventory.", "Dialogue", "1 / 3", "A box of worms."),
      ("Unsigned copied witness statements sit beside the fire report.", "Evidence montage", "2 / 4", "None"),
      ("A maintenance diagram shows no active wiring in the named corridor wall.", "Contradiction", "3 / 5", "None"),
      ("Three death notices show the same narrow strip cut away.", "Reveal", "4 / 5", "The part where a name should have been.")]),
    (3, "29-33", STATION_SCENE, "cinematic", "steady",
     "Move Daniel from archival suspicion into physical risk at 11:41 PM.",
     "Feel the wet, unstable station and Daniel's dry professional humor.", "2 -> 3", "question",
     "What remains inside before the clearance crew arrives?",
     "A vertical descent from leaking roof to Daniel to the permit grounds the space.",
     "Daniel carries permits, flashlight, notebook supplies, and gloves; it is 11:41 PM.",
     [("Rain enters through holes in the abandoned station roof.", "Establishing", "2 / 3", "11:41 PM"),
      ("Daniel advances with flashlight between his teeth and permits under one arm.", "Character action", "2 / 4", "None"),
      ("He considers dying of tetanus before finishing the accession log.", "Dry humor", "1 / 3", "None")]),
    (4, "35-39", STATION_SCENE, "cinematic", "expansive",
     "Establish the 2026 station as ruined grandeur and separate its clock from the cafe clock.",
     "Absorb scale, loss, redevelopment pressure, and the stopped 12:07 omen.", "2 -> 4", "reveal",
     "Daniel finds the Cafe Siete sign beside the ticket hall.",
     "Use one large architectural field and one low strip; no overlap is needed.",
     "Large station clock is above the ticket hall and stopped at 12:07.",
     [("The ruined junction opens in an extreme-wide view: arches, tile, beams, boarded windows.", "Establishing", "2 / 5", "None"),
      ("The large station clock hangs above the ticket hall at 12:07.", "Object reveal", "3 / 5", "None"),
      ("Daniel's light finds the cracked CAFE SIETE sign.", "Discovery", "3 / 4", "\"Cafe Siete.\"")]),
    (5, "41-49", STATION_SCENE, "suspense", "expansive",
     "Introduce the first scratched message as an unexplained personal clue.",
     "Pause on TOMAS long enough for the name to become a threat and invitation.", "3 -> 4", "reveal",
     "The gate opens onto the dead cafe.",
     "Let the painted glass dominate; a narrow reaction inset may overlap empty paint only.",
     "The TOMAS scratch predates Daniel's visit; its author remains unknown.",
     [("Daniel sees TOMAS scratched into painted-over door glass.", "Reveal", "4 / 5", "TOMAS."),
      ("He photographs and logs the shallow, grime-filled letters.", "Evidence action", "2 / 4", "None"),
      ("Daniel eases the twisted grille aside.", "Transition", "3 / 4", "SFX: KRRRNN")]),
    (6, "51-63", STATION_SCENE, "cinematic", "steady",
     "Map the ruined cafe and lead Daniel to the brass token.",
     "Understand the customer counter, kitchen doorway, and separate narrow hatch before time overlaps them.", "2 -> 3", "question",
     "What made the click after Daniel handled the token?",
     "Use a clear environment panel followed by a descending object-search sequence.",
     "Counter, doorway, and closed service hatch are established as separate structures.",
     [("The ruined cafe interior shows counter, missing stools, case, doorway, and closed hatch.", "Establishing", "2 / 5", "None"),
      ("Daniel steps over plaster and follows a brass glint under the counter lip.", "Discovery", "2 / 3", "None"),
      ("He sets the folder dry, places the flashlight, and pulls on cotton gloves.", "Character action", "1 / 4", "None"),
      ("The corroded token comes free in his gloved fingers.", "Object detail", "3 / 4", "\"Cute.\"")]),
    (7, "61-75", STATION_SCENE, "suspense", "steady",
     "Connect token handling to the clock movement without claiming causality.",
     "Hear the impossible before seeing it.", "3 -> 5", "reveal",
     "The smaller cafe clock snaps to 12:00.",
     "Three quiet details feed a tall clock panel; keep token and cafe clock visually distinct.",
     "Token is dropped only after the light burst on the next page; cafe clock begins at 12:07.",
     [("Token face shows cup and CAFE SIETE.", "Object detail", "2 / 3", "None"),
      ("Reverse shows the number 7 and green edge corrosion.", "Object detail", "2 / 3", "None"),
      ("A dry mechanical click arrests Daniel.", "Reaction", "3 / 4", "SFX: CLICK"),
      ("The smaller brass-rimmed clock above the cafe door shudders at 12:07.", "Reveal", "4 / 5", "None"),
      ("Its long hand snaps upright to 12:00.", "Impact", "5 / 5", "12:00")]),
    (8, "77-87", STATION_SCENE, "reveal", "impact",
     "Open the time connection through simultaneous light, heat, sound, and contradiction.",
     "Experience sensory overload while retaining the ruined 2026 anchors.", "4 -> 5", "question",
     "Who is moving inside the restored side of Cafe Siete?",
     "A border-breaking light/steam event crosses smaller ruined-state anchors; reading order remains top-left to bottom-right.",
     "Daniel drops the token; his stools, tile, and painted door remain ruined while 1986 becomes perceptible across shared surfaces.",
     [("Light bursts across the counter as Daniel drops the token.", "Impact", "5 / 5", "None"),
      ("Coffee steam, butter, bread, coats, voices, and an announcement rush in.", "Sensory montage", "4 / 4", "None"),
      ("The pastry case beyond the counter gleams full of rolls.", "Past-state reveal", "4 / 5", "None"),
      ("Daniel turns to broken stools and the still-painted door on his side.", "Contradiction", "4 / 5", "None")]),
    (9, "89-103", STATION_SCENE, "reveal", "expansive",
     "Reveal Tomas as the living human center of the impossible event.",
     "Move from visual recognition to imminent physical contact.", "4 -> 5", "threat",
     "The tray tilts toward the boundary.",
     "Give Tomas a dominant full-figure entrance with one hair/hand detail inset outside his face.",
     "Tomas wears the approved 1986 cafe clothing and carries sugared rolls on a brass tray.",
     [("Tomas stops mid-step with the bread tray, alive and warmly lit.", "Character reveal", "5 / 5", "None"),
      ("Daniel registers tied dark hair, green cord, flour, rolled sleeves, and apron.", "Recognition detail", "3 / 4", "None"),
      ("The tray begins to tilt between them.", "Action setup", "4 / 5", "None")]),
    (10, "95-105", STATION_SCENE, "action", "impact",
     "Make the first shared touch undeniable and stop the fall.",
     "Feel a suspended instant of danger, contact, and mutual shock.", "5 -> 4", "emotional_turn",
     "The bright brass tray remains shared after their hands separate.",
     "Use a large diagonal tray catch with an overlapping fingertip close-up and two small reaction cuts.",
     "The customer counter/tray contact is initially stable; no pain occurs yet.",
     [("Daniel and Tomas catch opposite edges of the tilting tray.", "Action", "5 / 5", "None"),
      ("Their fingers touch against bright brass.", "Contact detail", "5 / 5", "None"),
      ("Daniel freezes.", "Reaction", "4 / 4", "None"),
      ("Tomas freezes, then steadies the tray against his hip.", "Reaction/action", "4 / 4", "None")]),
    (11, "107-131", STATION_SCENE, "comedy", "steady",
     "Let Tomas manage fear through humor while Daniel defaults to professional literalness.",
     "Release tension without making the impossible feel safe.", "3 -> 2", "joke",
     "Daniel's explanation of the gloves explains almost nothing.",
     "Use clean alternating reactions and preserve room context behind each speaker.",
     "Daniel remains on the ruined customer side; Tomas remains on the working 1986 side.",
     [("Tomas studies Daniel's glove, face, and ruined background.", "Reaction", "3 / 4", "\"You are not from the evening train.\""),
      ("Daniel's mind collapses into etiquette.", "Dialogue", "2 / 3", "\"No.\""),
      ("Tomas laughs like steam escaping a kettle.", "Reaction", "2 / 4", "\"Good. I would worry about the evening train if it started bringing men dressed like museum ghosts.\""),
      ("Daniel adjusts his slipping glasses.", "Dialogue", "1 / 3", "\"Museum conservator.\" / \"It explains the gloves.\"")]),
    (12, "133-167", STATION_SCENE, "dialogue", "steady",
     "Prove that the two men perceive different eras and obtain Tomas's exact date.",
     "Shift from comic testing to sober temporal evidence.", "2 -> 4", "reveal",
     "Tomas states October 17, 1986 and asks for Daniel's turn.",
     "A wide split-era room panel anchors the dialogue; smaller face cuts tighten as the answer approaches.",
     "1986 windows are whole and populated; Daniel's surrounding cafe remains ruined.",
     [("A whole 1986 station operates behind Tomas while Daniel's side stays dark and broken.", "Establishing contradiction", "3 / 5", "Two times met at the counter and refused to agree on the room."),
      ("Daniel asks the only useful question.", "Dialogue", "3 / 4", "\"What year is it?\""),
      ("Tomas tests drunk, injured, and possessed explanations.", "Comedy dialogue", "2 / 3", "\"Possessed?\" / \"I work for a museum.\" / \"So maybe.\""),
      ("Tomas gives the date and place with deliberate calm.", "Evidence reveal", "4 / 5", "\"Nineteen eighty-six. October seventeenth. San Aurelio Junction. Cafe Siete. Midnight shift, unfortunately. Your turn.\"")]),
    (13, "169-187", STATION_SCENE, "reveal", "steady",
     "Answer Tomas with 2026 and begin the visible countdown.",
     "Make the forty-year gulf tangible through material change and silence.", "4 -> 5", "threat",
     "The cafe clock reaches 12:01 and Tomas says it has been broken for two years.",
     "Let a coffee-ring transformation inset overlap the shared counter field without covering hands or clock.",
     "Shared wood is smooth; a wet 1986 coffee ring dries immediately on Daniel's side.",
     [("Daniel grips the shared counter as a wet coffee ring appears near his thumb.", "Material event", "3 / 4", "None"),
      ("The ring dries to a pale stain on the 2026 side.", "Transformation detail", "4 / 5", "None"),
      ("Daniel states his year.", "Dialogue reveal", "4 / 5", "\"Twenty twenty-six.\""),
      ("The clock advances to 12:01.", "Countdown", "5 / 5", "12:01 / \"That clock has been broken for two years.\"")]),
    (14, "189-205", STATION_SCENE, "dialogue", "steady",
     "Exchange names and connect Tomas to the unexplained door scratch.",
     "Let attraction and historical dread arrive in the same beat.", "3 -> 5", "reveal",
     "Daniel says he found Tomas's name.",
     "Use an intimate name exchange, then a cold match cut to TOMAS on painted glass.",
     "Tomas does not yet know where his name was found.",
     [("Daniel recognizes Tomas's guarded curiosity.", "Reaction", "3 / 4", "None"),
      ("Daniel introduces himself.", "Dialogue", "3 / 4", "\"My name is Daniel Soriano.\""),
      ("Tomas answers with a smaller deliberate smile.", "Dialogue", "3 / 5", "\"Tomas Rivera.\""),
      ("The scratched TOMAS on 2026 glass cuts through Daniel's recognition.", "Match-cut reveal", "5 / 5", "TOMAS."),
      ("Daniel tells Tomas what he found.", "Dialogue", "4 / 4", "\"Sorry. I mean, I found your name.\"")]),
    (15, "207-235", STATION_SCENE, "comedy", "steady",
     "Test the door clue while deepening their chemistry without resolving authorship.",
     "Balance dread with Tomas's theatrical offense.", "3 -> 3", "joke",
     "Their banter steadies the room just before the boundary fails.",
     "Alternate the two door states and face reactions; no panel overlap.",
     "Painted 2026 glass reads TOMAS; clear 1986 glass reflects Tomas; Tomas denies writing it.",
     [("Daniel points to painted glass while Tomas turns toward clear glass in his era.", "Parallel-state action", "3 / 5", "None"),
      ("Tomas sees only his reflection in the clear 1986 door.", "Visual contradiction", "3 / 4", "\"I did not write that.\""),
      ("Daniel offers that Tomas may write it later.", "Dialogue", "3 / 3", "\"Maybe you do later.\""),
      ("Tomas rejects the idea with theatrical offense.", "Comedy", "2 / 4", "\"Do I seem like a man who scratches my own name into doors?\""),
      ("Daniel lands the wax-paper accusation.", "Comedy", "2 / 4", "\"You seem more likely to write it on wax paper and hide it in someone's lunch.\" / \"That is a private accusation.\"")]),
    (16, "237-255", STATION_SCENE, "action", "impact",
     "Break the stable customer-counter contact and redirect them to the service hatch.",
     "Turn flirtation into sudden pain and a new rule.", "3 -> 5", "reveal",
     "The service hatch opens by itself.",
     "Use a diagonal counter-failure panel, overlapping wrist-contact inset, and a tall hatch-opening payoff.",
     "At 12:02 Daniel's left hand sinks; Tomas catches his wrist; both feel pain; no injury is established.",
     [("The clock reaches 12:02 and the lights flicker.", "Countdown", "4 / 4", "12:02"),
      ("The customer counter shifts and Daniel's left hand sinks into unstable wood.", "Boundary failure", "5 / 5", "None"),
      ("Tomas catches Daniel's wrist through cotton.", "Contact action", "5 / 5", "None"),
      ("Warm fingers and a living pulse register for less than a breath.", "Contact detail", "4 / 5", "None"),
      ("Pain snaps up Daniel's arm as Tomas recoils.", "Reaction", "5 / 5", "None"),
      ("The narrow service hatch slides open behind Tomas.", "Reveal", "5 / 5", "SFX: SHHK")]),
    (17, "255-267", STATION_SCENE, "comedy", "steady",
     "Clarify the stable hatch route and preserve the two-sided cafe geography.",
     "Recover breath while learning the next physical rule.", "4 -> 3", "question",
     "Tomas offers a fresh roll through the hatch.",
     "A clear route diagram in action: Tomas through his doorway, Daniel around his counter, meeting at the hatch.",
     "Daniel never enters 1986; broken tile remains beneath his boots; hatch lower frame is charred only in 2026.",
     [("Clean 1986 hatch and charred 2026 hatch occupy the same boundary.", "Environment contrast", "4 / 5", "None"),
      ("Tomas names it the proper counter; Daniel corrects him.", "Comedy dialogue", "2 / 3", "\"I think the haunted cafe wants us to use the proper counter.\" / \"Service window.\""),
      ("Tomas carries the tray through his kitchen doorway.", "Spatial action", "2 / 4", "None"),
      ("Daniel collects folder and flashlight, walks around his ruined counter, and faces Tomas at the hatch.", "Spatial action", "2 / 5", "None")]),
    (18, "269-283", STATION_SCENE, "suspense", "expansive",
     "Begin the forward-transfer experiment and hold the perfect bread between eras.",
     "Make the shared saucer feel intimate before time exacts its fee.", "3 -> 5", "threat",
     "Tomas releases the saucer.",
     "Two broad hand-and-object panels followed by a suspended near-silent release detail.",
     "Tomas uses brass tongs; roll is fresh on a white saucer; both hold it before Daniel draws it fully into 2026.",
     [("Tomas selects one sugared roll with brass tongs.", "Object action", "2 / 4", "None"),
      ("He pushes the white saucer into the narrow hatch.", "Transfer setup", "3 / 4", "None"),
      ("Daniel takes the near rim while Tomas holds the far rim.", "Shared contact", "4 / 5", "None"),
      ("The bread remains perfect for one impossible second.", "Suspense", "4 / 5", "None"),
      ("Tomas lets go.", "Decision detail", "5 / 5", "None")]),
    (19, "273-289", STATION_SCENE, "reveal", "impact",
     "Show the complete aging cost of forward transfer.",
     "Replace wonder with material horror and Tomas's first unguarded fear.", "5 -> 5", "emotional_turn",
     "Daniel believes Tomas because the bread becomes evidence.",
     "A dominant transformation panel may bleed; two small before/after detail insets must not hide Daniel's hands or Tomas's face.",
     "Bread shrinks, darkens, cracks, and flakes; saucer yellows and gains one hairline glaze fracture.",
     [("Time takes its fee across bread and saucer as they clear into 2026.", "Transformation reveal", "5 / 5", "Time took its fee."),
      ("The ruined roll flakes under Daniel's gloved fingertip.", "Evidence detail", "4 / 5", "None"),
      ("Tomas's cheer finally falters.", "Reaction", "4 / 5", "\"That was fresh.\""),
      ("Daniel answers without doubt.", "Dialogue", "3 / 4", "\"I believe you.\"")]),
    (20, "291-321", STATION_SCENE, "dialogue", "steady",
     "Launch the reverse-transfer test and distinguish the archival sleeve from the later notebook page.",
     "Watch Daniel turn fear into a controlled experiment.", "3 -> 4", "question",
     "Will future paper survive in 1986?",
     "Use a clean procedural sequence with a small announcement strip above, never confusing paper items.",
     "At 12:03 Daniel chooses one blank acid-free sleeve, not his notebook page, phone, or flashlight.",
     [("A 1986 announcement reports the delayed southbound service through rain.", "Audio clue", "2 / 3", "Last southbound service delayed."),
      ("The cafe clock reaches 12:03.", "Countdown", "3 / 4", "12:03"),
      ("Daniel rejects phone and flashlight, selects a blank acid-free sleeve, and writes.", "Evidence action", "3 / 5", "DANIEL SORIANO / SAN AURELIO MUNICIPAL MUSEUM / 2026 / I am real."),
      ("He folds the sleeve once and passes it through the hatch.", "Transfer action", "4 / 5", "None"),
      ("Tomas catches the sleeve.", "Action", "4 / 4", "None")]),
    (21, "321-343", STATION_SCENE, "dialogue", "expansive",
     "Prove backward transfer and let reciprocal recognition become the chapter's emotional center.",
     "Feel two people choose to treat each other as real.", "3 -> 5", "emotional_turn",
     "The clock reaches 12:04 after Tomas pockets the sleeve.",
     "Center the crisp white paper between the men; a quiet eye close-up may overlap background only.",
     "The sleeve remains white and crisp in 1986 and stays in Tomas's apron pocket.",
     [("The future sleeve stays white and crisp against the old cafe.", "Proof reveal", "4 / 5", "None"),
      ("Tomas calls the paper expensive; Daniel explains archival means it lasts.", "Dialogue", "2 / 3", "\"This paper feels expensive.\" / \"It means it lasts.\""),
      ("Tomas rereads Daniel's exposed claim.", "Emotional beat", "4 / 5", "\"I am real.\""),
      ("He pockets the sleeve and returns the recognition.", "Emotional turn", "5 / 5", "\"Then I am real too.\""),
      ("The clock reaches 12:04.", "Countdown", "4 / 4", "12:04")]),
    (22, "345-361", STATION_SCENE, "comedy", "steady",
     "Bring Lilia's ordinary work voice into the miracle and deepen Daniel's attachment.",
     "Let warmth survive inside the countdown.", "3 -> 4", "threat",
     "Daniel asks whether the connection happens every night.",
     "Use a rolling flashlight diagonal to bridge rooms; keep Lilia off-panel as required by the manuscript.",
     "Lilia is heard from the 1986 kitchen and is Tomas's aunt by chosen family, not blood.",
     [("Lights flicker harder and Daniel's flashlight rolls off the sill.", "Action", "3 / 4", "SFX: CLACK"),
      ("Lilia calls from deeper in the kitchen without appearing.", "Off-panel dialogue", "2 / 3", "\"Tomas! Are you charming the midnight customers again?\""),
      ("Tomas answers with embarrassed delight.", "Comedy dialogue", "2 / 4", "\"Only the impossible ones, Tiya Lilia.\" / \"Impossible customers pay first.\""),
      ("Tomas explains chosen family by volume.", "Dialogue", "2 / 4", "\"My aunt. Not by blood. By volume.\""),
      ("Daniel memorizes flour, uneven sleeves, bright eyes, and Tomas's mouth.", "Intimate observation", "4 / 5", "None")]),
    (23, "363-375", STATION_SCENE, "suspense", "expansive",
     "Convert seven strange minutes into a two-minute deadline.",
     "Feel the door begin closing around a connection neither man wants to lose.", "3 -> 5", "decision",
     "Daniel decides to question Tomas quickly.",
     "Use a dominant 12:05 clock field with both men small beneath it; no decorative clutter.",
     "No nightly recurrence is proven; the 12:07 end is Daniel's evidence-based hypothesis.",
     [("Daniel asks whether this happens every night; Tomas jokes he would charge admission.", "Dialogue", "2 / 3", "None"),
      ("Daniel proposes they may have until 12:07.", "Reasoning", "4 / 5", "\"Maybe we have until then.\""),
      ("The cafe clock reaches 12:05 above them.", "Countdown reveal", "5 / 5", "12:05 / Two minutes left.")]),
    (24, "375-391", STATION_SCENE, "dialogue", "compressed",
     "Gather actionable clues under pressure without treating any clue as an answer.",
     "Feel Tomas's comic inventory harden into danger.", "4 -> 5", "threat",
     "Daniel writes SOUTHBOUND SIGNAL and BROKER as separate leads.",
     "Use a six-beat escalating montage around one central Tomas panel; overlaps may touch backgrounds only.",
     "Arturo is a reported broker in a white suit; Chapter 1 does not establish guilt.",
     [("Daniel asks for anything unusual involving object, date, event, or building.", "Dialogue", "4 / 4", "None"),
      ("Lost suitcase and a woman crying into soup flash through Tomas's account.", "Reported montage", "2 / 2", "None"),
      ("Two soldiers argue over cards.", "Reported montage", "2 / 2", "None"),
      ("A broker in a white suit holds undrunk coffee.", "Reported clue", "4 / 5", "None"),
      ("A failed southbound signal and burned first bread tray complete the list.", "Reported clue", "4 / 5", "None"),
      ("Tomas adds the beautiful museum ghost; Daniel writes SIGNAL then BROKER.", "Emotional/clue turn", "4 / 5", "\"Also, a beautiful museum ghost arrived from the future.\"")]),
    (25, "383-397", STATION_SCENE, "suspense", "steady",
     "Name Arturo while the connection begins visibly collapsing.",
     "Keep suspicion provisional and redirect urgency to the clock.", "4 -> 5", "threat",
     "12:06 arrives as lights begin dying behind Tomas.",
     "A white-suit report inset sits behind Tomas's face, followed by pencil and dust details leading to the clock.",
     "Arturo has visited station offices for a month; failed signal and broker remain leads only.",
     [("Tomas names Arturo Salcedo and describes his month of office visits.", "Reported clue", "4 / 5", "\"Smiles like a knife under a napkin.\""),
      ("Daniel records Arturo beside the failed signal.", "Evidence action", "3 / 4", "Two things to check. Neither was an answer."),
      ("The pencil lead snaps.", "Omen detail", "4 / 4", "SFX: TIK"),
      ("Dust rises from Daniel's floorboards as if the building exhales.", "Boundary omen", "4 / 5", "None"),
      ("The clock reaches 12:06.", "Countdown", "5 / 5", "12:06")]),
    (26, "399-415", STATION_SCENE, "suspense", "expansive",
     "Strip away Tomas's comic mask and secure the next meeting.",
     "Make Daniel's name, spoken in fear, turn the impossible into a personal promise.", "4 -> 5", "decision",
     "Tomas agrees to return tomorrow at midnight.",
     "Let lights vanish in narrow vertical cuts behind a dominant Tomas reaction.",
     "The return is a promise, not proof that contact will recur.",
     [("Lights go out one by one behind Tomas.", "Escalation", "4 / 5", "None"),
      ("Fear reaches Tomas's face without disguise.", "Reaction", "5 / 5", "\"Daniel.\""),
      ("Daniel asks Tomas to return tomorrow at midnight.", "Decision", "5 / 5", "\"Tomorrow. Come back tomorrow at midnight.\""),
      ("Tomas's shaken private smile returns.", "Emotional turn", "4 / 5", "\"Obviously.\"")]),
    (27, "417-429", STATION_SCENE, "dialogue", "steady",
     "Create the distinct return-message paper and establish safe fingertip contact through the hatch.",
     "Move from operational secrecy to wordless intimacy.", "4 -> 5", "emotional_turn",
     "Tomas takes out his pencil to reply.",
     "Keep the three written instructions legible in a dedicated paper panel; end with the touch detail.",
     "This is a torn notebook page, not the archival sleeve already in Tomas's pocket.",
     [("Daniel tears a page from his notebook and writes with the broken pencil.", "Writing action", "3 / 4", "DO NOT TELL ANYONE ABOUT ME. / KEEP THIS HIDDEN. / COME BACK TOMORROW."),
      ("He pushes the notebook page through the service hatch.", "Transfer action", "4 / 4", "None"),
      ("Tomas takes it and their fingertips brush through the stable hatch.", "Contact", "5 / 5", "None"),
      ("No pain comes, only warmth.", "Emotional beat", "4 / 5", "Only warmth.")]),
    (28, "431-437", STATION_SCENE, "suspense", "impact",
     "Race the returning reply against the final clock click.",
     "Hold the paper physically between survival and loss.", "4 -> 5", "threat",
     "The clock reaches 12:07 before Daniel can secure the page.",
     "A long diagonal paper movement crosses three small object/reaction cuts; the charred split remains the focal obstacle.",
     "Tomas writes on Daniel's notebook page; it yellows only after he releases it into 2026 and catches in the charred lower-frame split.",
     [("Tomas bends over the page and writes while Daniel watches the clock.", "Writing/suspense", "4 / 5", "None"),
      ("The paper slides back; Tomas releases it.", "Transfer action", "4 / 5", "None"),
      ("It yellows as it clears into 2026.", "Transformation", "5 / 5", "None"),
      ("One corner catches in the charred split as Daniel reaches.", "Threat", "5 / 5", "None"),
      ("The cafe clock clicks to 12:07.", "Countdown impact", "5 / 5", "12:07 / SFX: CLICK")]),
    (29, "439-447", STATION_SCENE, "reveal", "impact",
     "Collapse the parallel cafe and leave Daniel in the 2026 ruin.",
     "Experience the connection's absence as a physical blow.", "5 -> 5", "emotional_turn",
     "Daniel remains with his hand raised toward where Tomas stood.",
     "Use a full-width vanishing event, then a severe black field with two small ruined-state cuts.",
     "1986 kitchen and pastry case vanish; service hatch is closed; 2026 kitchen contains old ash.",
     [("The lit 1986 cafe dies in a single collapsing field.", "Smash transition", "5 / 5", "The cafe died."),
      ("Cold rain and darkness return around Daniel.", "Sensory reversal", "5 / 5", "None"),
      ("The service hatch is closed over a black kitchen of old ash.", "State reveal", "5 / 5", "None"),
      ("Daniel stands alone with his hand still raised.", "Silence", "5 / 5", "None")]),
    (30, "449-463", STATION_SCENE, "reveal", "expansive",
     "Recover the aged reply and preserve Tomas's promised humor after disappearance.",
     "Let relief and grief occupy the same fragile object.", "4 -> 5", "emotional_turn",
     "Daniel's laugh breaks in the middle.",
     "Use a quiet object-led sequence; the handwritten reply receives the largest readable space.",
     "Notebook page is yellowed, brittle, curled, pencil-faded, and smoke-stained after full return.",
     [("The pale page corner comes free and settles on Daniel's side.", "Object recovery", "4 / 5", "None"),
      ("Daniel recognizes his notebook page, forty years older.", "Evidence reveal", "4 / 5", "None"),
      ("A brown smoke-smelling stain crosses the bottom corner.", "Clue detail", "4 / 4", "None"),
      ("Tomas's different handwriting appears below Daniel's warning.", "Emotional reveal", "5 / 5", "I will bring better bread.")]),
    (31, "465-469", STATION_SCENE, "cinematic", "expansive",
     "Show Daniel convert an emotional shock back into careful preservation.",
     "Feel restraint fail for one sound, then return through practiced hands.", "4 -> 4", "question",
     "Why does Daniel turn the flashlight toward the cafe door?",
     "One reaction panel, one careful hand panel, one directional flashlight panel.",
     "Daniel folds the aged notebook page carefully and places it in an acid-free sleeve.",
     [("Daniel laughs once and the sound breaks in the middle.", "Reaction", "4 / 5", "None"),
      ("He folds the page with a conservator's care and sleeves it.", "Preservation action", "3 / 5", "None"),
      ("Daniel retrieves the flashlight and aims it toward the cafe door.", "Transition", "4 / 5", "None")]),
    (32, "471-477", STATION_SCENE, "reveal", "impact",
     "Reveal the canon-correct final fire warning beneath TOMAS.",
     "Transform the romantic promise into immediate historical danger.", "4 -> 5", "threat",
     "The station clock remains fixed at 12:07 beyond the next turn.",
     "Use TOMAS as the entry anchor, then a dust-shift overlay revealing the second line without covering either message.",
     "The two scratches are separate; author, date, method, and intended recipient remain unknown.",
     [("The flashlight catches TOMAS in the painted glass.", "Recall", "4 / 5", "TOMAS."),
      ("Dust shifts beneath it and exposes a separate scratched line.", "Reveal setup", "5 / 5", "None"),
      ("The full warning becomes legible.", "Threat reveal", "5 / 5", "FIRE STARTS IN THE SERVICE CORRIDOR."),
      ("Daniel stops breathing.", "Reaction", "5 / 5", "None")]),
    (33, "479-482", STATION_SCENE, "cinematic", "impact",
     "End Chapter 1 on the large station clock and the seven-minute limit.",
     "Leave the reader with urgency, uncertainty, and the promise of another midnight.", "5 -> 5", "none",
     "End immediately; no teaser or preview follows.",
     "Use one large exterior/interior architectural image and one inset clock detail; no extra clue text.",
     "Large station clock is separate from the cafe clock and remains stopped at 12:07 in 2026.",
     [("Daniel stands small beneath the ruined station architecture, holding the sleeved reply.", "Closing image", "5 / 5", "None"),
      ("The large station clock remains fixed at 12:07.", "Final object", "5 / 5", "12:07")]),
]

# Expand the final emotional aftermath into 36 pages without changing event order.
# Pages 30-33 above become pages 33-36; the inserted pages isolate evidence and reactions.
INSERTS = [
    (30, "449-459", STATION_SCENE, "suspense", "expansive",
     "Hold Daniel alone before the returned page becomes fully readable.",
     "Let absence settle before offering proof that Tomas reached him.", "5 -> 4", "reveal",
     "The returned page is Daniel's, forty years older.",
     "Two large silent panels and one object detail; no overlap.",
     "Daniel is alone; service hatch is closed; the paper clears only after the connection ends.",
     [("Daniel remains motionless in the ruined cafe.", "Silence", "5 / 5", "None"),
      ("The pale corner frees itself from the charred split and settles on the sill.", "Object movement", "4 / 5", "None"),
      ("Daniel sees his notebook page aged by forty years.", "Reveal", "5 / 5", "None")]),
    (31, "457-463", STATION_SCENE, "reveal", "expansive",
     "Inspect the returned page and reveal Tomas's reply.",
     "Turn physical decay into intimate reassurance.", "4 -> 5", "emotional_turn",
     "Daniel's laugh follows on the next page.",
     "A broad page-detail field carries the writing; two evidence insets sit outside the message area.",
     "Edges yellow, pencil fades, and one brown smoke-smelling stain crosses the bottom corner.",
     [("Yellowed edges and faded pencil prove the page's age.", "Evidence detail", "4 / 4", "None"),
      ("A brown stain at the lower corner smells faintly of smoke.", "Clue detail", "4 / 5", "None"),
      ("Tomas's handwriting appears beneath Daniel's warning.", "Emotional reveal", "5 / 5", "I will bring better bread.")]),
    (32, "465-469", STATION_SCENE, "cinematic", "expansive",
     "Show Daniel's cracked relief and immediate conservator response.",
     "Let emotion escape once, then return to precise care.", "4 -> 4", "question",
     "Daniel directs the flashlight toward the cafe door.",
     "One face panel, one delicate hand panel, one strong beam-direction transition.",
     "The aged notebook page is folded and placed in an acid-free sleeve; it is not the first sleeve Tomas kept.",
     [("Daniel laughs once and the sound breaks in the middle.", "Reaction", "4 / 5", "None"),
      ("He folds the page with a conservator's care and places it in a new acid-free sleeve.", "Preservation action", "3 / 5", "None"),
      ("He retrieves the flashlight and turns its beam toward the cafe door.", "Transition", "4 / 5", "None")]),
]

# Replace the compressed original pages 30-33 with the three inserts and renumber the
# warning and closing pages to 35-36.
PAGES = [page for page in PAGES if page[0] < 30]
PAGES.extend(INSERTS)
PAGES.extend([
    (33, "471-473", STATION_SCENE, "suspense", "expansive",
     "Return to the original TOMAS scratch before exposing new information.",
     "Make the familiar name feel newly vulnerable after meeting its owner.", "4 -> 5", "reveal",
     "Dust shifts below TOMAS.",
     "One dominant door-glass panel and one close reaction; preserve large empty space beneath the name.",
     "TOMAS was already present before the contact and remains a separate scratch.",
     [("The flashlight beam finds TOMAS waiting in the painted glass.", "Recall", "4 / 5", "TOMAS."),
      ("Daniel holds the sleeved reply and stares at the name.", "Reaction", "4 / 5", "None")]),
    (34, "475-477", STATION_SCENE, "reveal", "impact",
     "Expose the canon-correct fire warning as the chapter's final threat.",
     "Turn promise into urgent danger without assigning culprit or fate.", "5 -> 5", "threat",
     "Daniel's reaction and the station clock wait on the last two pages.",
     "A dust-shift overlay can break the frame; the warning itself must remain fully unobstructed and readable.",
     "Warning reads exactly FIRE STARTS IN THE SERVICE CORRIDOR; authorship and timing remain unknown.",
     [("Dust shifts beneath TOMAS and reveals a second scratch.", "Reveal setup", "5 / 5", "None"),
      ("The full separate warning fills the page's dominant field.", "Threat reveal", "5 / 5", "FIRE STARTS IN THE SERVICE CORRIDOR.")]),
    (35, "479", STATION_SCENE, "cinematic", "expansive",
     "Hold Daniel's bodily response after the warning.",
     "Give the threat one silent human consequence before the final clock image.", "5 -> 5", "threat",
     "The final page reveals the large station clock at 12:07.",
     "Use a single near-silent portrait with hard flashlight contrast; no overlap.",
     "Daniel knows the warning but still does not know the fire date, cause, victims, or author.",
     [("Daniel stops breathing with the warning reflected in his glasses.", "Reaction", "5 / 5", "None")]),
    (36, "481-482", STATION_SCENE, "cinematic", "impact",
     "End on the separate large station clock and the seven-minute limit.",
     "Leave urgency, uncertainty, and the promise of another midnight.", "5 -> 5", "none",
     "End Chapter 1 immediately; no teaser, preview, or Chapter 2 beat follows.",
     "One full-page architectural closing image with the clock as the focal point; Daniel may remain small below.",
     "Large station clock is above the ticket hall, separate from the cafe clock, and fixed at 12:07 in 2026.",
     [("The ruined station contains Daniel beneath the stopped large clock.", "Closing image", "5 / 5", "None"),
      ("The clock face holds at 12:07 as rain continues.", "Final object", "5 / 5", "12:07")]),
])


def panel_id(page_number: int, index: int) -> str:
    return f"c001-p{page_number:03d}-{index:02d}"


def render_page(page) -> str:
    (number, lines, scene, intent, pacing, purpose, effect, curve, turn_kind,
     turn_setup, layout, continuity, panels) = page
    ids = [panel_id(number, i) for i in range(1, len(panels) + 1)]
    rows = []
    for pid, (event, event_type, score, text_value) in zip(ids, panels):
        rows.append(f"| `{pid}` | {event} | {event_type} | {score} | {text_value} |")
    return f"""## Page {number:03d} - {purpose.split('.')[0]}

- **Page ID:** `chapter-001-page-{number:03d}`
- **Source:** `{scene}`, approved manuscript lines {lines}
- **Intent / pacing:** {intent.title()} / {pacing}
- **Purpose:** {purpose}
- **Reader effect:** {effect}
- **Emotional curve:** {curve}
- **Reading sequence:** {' -> '.join(f'`{value}`' for value in ids)}
- **Layout direction:** {layout}
- **Dialogue load:** {sum(1 for panel in panels if panel[3] != 'None')} assigned text beat(s)

| Panel | Dominant event | Type | Intensity / importance | Assigned text |
|---|---|---|---|---|
{chr(10).join(rows)}

**Continuity out:** {continuity}  
**Page turn ({turn_kind}):** {turn_setup}
"""


def render_group(start: int, end: int) -> str:
    selected = [page for page in PAGES if start <= page[0] <= end]
    body = "\n".join(render_page(page) for page in selected)
    return f"""# Chapter 001 Storyboard Beats - Pages {start:03d}-{end:03d}

**Version:** v001  
**Status:** PROPOSED - NOT ACTIVE  
**Authority:** approved canon v002 and locked manuscript v001  
**Reading direction:** left-to-right

Internal panel IDs define workflow order only and must never be rendered. Panel counts are situation-driven candidates, not a chapter quota; later panel direction may revise them while preserving all dominant events and reading order.

{body}
"""


assert len(PAGES) == 36
assert [page[0] for page in PAGES] == list(range(1, 37))

groups = [(1, 9), (10, 18), (19, 27), (28, 36)]
component_paths = []
for start, end in groups:
    path = STORYBOARD / f"chapter-001-pages-{start:03d}-{end:03d}-v001.md"
    write(path, render_group(start, end))
    component_paths.append(path)

turn_lines = [
    "# Chapter 001 Page Turns And Continuity Handoffs",
    "",
    "**Version:** v001  ",
    "**Status:** PROPOSED - NOT ACTIVE  ",
    "**Reading direction:** left-to-right",
    "",
    "Every page turn follows the approved manuscript order. `Payoff` means the next page fulfills the setup; it does not authorize new story content.",
    "",
    "| Page | Kind | Setup | Payoff on next page |",
    "|---:|---|---|---|",
]
for page in PAGES:
    kind = page[8]
    payoff = "No" if page[0] == 36 or kind == "none" else "Yes"
    turn_lines.append(f"| {page[0]:03d} | {kind} | {page[9]} | {payoff} |")
turn_lines.extend([
    "",
    "## Global Handoffs",
    "",
    "- The 2026 station clock above the ticket hall and the smaller cafe clock above the cafe door are always separate objects.",
    "- Daniel remains in the ruined 2026 cafe. Tomas remains in working 1986. Shared surfaces permit sight, sound, and limited contact, never bodily passage.",
    "- The customer counter is initially stable, fails at 12:02, and is abandoned for the narrow service hatch beside the full kitchen doorway.",
    "- The fresh bread and saucer age only after forward transfer. The first acid-free sleeve remains crisp in 1986 and stays with Tomas.",
    "- The later torn notebook page is a different object. It returns, catches in the charred hatch split, and finishes aging after the connection closes.",
    "- Clock progression is 12:00 through 12:07 in order. No page may imply a longer or shorter first contact.",
    "- `TOMAS` and `FIRE STARTS IN THE SERVICE CORRIDOR` are separate scratches. Their author and timing remain unknown.",
    "- Arturo and the failed signal remain reported leads, not solutions. No fire culprit, exact date, victim list, or fate is invented.",
    "",
    "## Overlap Rules",
    "",
    "Overlap candidates are limited to Pages 002, 008, 009, 010, 013, 016, 019, 022, 024, 025, 028, 031, and 034. Each later panel plan must declare frame/clip geometry, z-index, focus, overlap permission, border or bleed state, explicit reading sequence, and dialogue-safe zones. No overlap may conceal a face, hand, clock state, paper identity, transfer state, scratch, or reader entry point.",
])
turn_path = STORYBOARD / "chapter-001-page-turns-v001.md"
write(turn_path, "\n".join(turn_lines))
component_paths.append(turn_path)

overview = """# Chapter 001 Storyboard Plan

**Version:** v001  
**Status:** PROPOSED - NOT ACTIVE  
**Scope:** Arc 1, Chapter 1 only  
**Source authority:** locked manuscript v001 and approved canon v002  
**Reading direction:** left-to-right  
**Page size:** 1654 x 2339 px  
**Page count:** 36 interior pages  
**Artwork:** not generated

## Purpose

Convert the locked Chapter 1 story into a professional manga rhythm without changing event order, evidence, dialogue facts, reveal ceiling, or knowledge states. The page plan uses situation-driven panel density, strong page turns, and controlled overlap candidates. Exact camera placement, geometry, safe zones, and image jobs remain later-stage work after explicit storyboard approval.

## Page Rhythm

| Sequence | Pages | Pacing | Reader effect |
|---|---:|---|---|
| Archive evidence | 001-002 | Steady to compressed | Trust Daniel's method, then discover deliberate omission |
| Ruined station approach | 003-007 | Cinematic to suspense | Establish geography, clocks, TOMAS, token, and the midnight trigger |
| First contact | 008-15 | Reveal to dialogue | Introduce Tomas, prove two eras, and connect him to the scratch |
| Boundary experiments | 016-22 | Impact to intimate | Learn surface rules, transfer costs, and reciprocal reality |
| Countdown and clues | 023-28 | Suspense to impact | Compress two minutes into leads, promise, touch, and closing race |
| Aftermath and warning | 029-36 | Impact to silence | Lose Tomas, recover his reply, and reveal the corridor threat |

## Adaptation Decisions

- Retain both locked source scenes in their approved order.
- Retain 36 interior pages within the accepted 32-40 page range.
- Apply no chapter-wide panel quota and no fixed panels-per-page rule.
- Use one dominant event per candidate panel; panel allocation may change during approved panel direction if page purpose and reading sequence remain intact.
- Preserve exact story facts and only assign manuscript text; no invented dialogue, fire culprit, fate, calendar date, or supernatural rule is introduced.
- Use controlled overlap only on identified pages where simultaneity, impact, transformation, or time pressure requires it.
- Keep artwork text-free and borderless in later generation. Geometry, clipping, borders, and lettering remain deterministic downstream stages.

## Components

1. `chapter-001-pages-001-009-v001.md`
2. `chapter-001-pages-010-018-v001.md`
3. `chapter-001-pages-019-027-v001.md`
4. `chapter-001-pages-028-036-v001.md`
5. `chapter-001-page-turns-v001.md`

## Approval Boundary

This storyboard is a review candidate. It does not set `active_storyboard_version`, `STORYBOARD_APPROVED`, `STORYBOARD_LOCKED`, `IMAGE_READY`, or `image_generation_enabled`. Panel direction and image-job release remain blocked until the user explicitly approves and locks this exact storyboard version.
"""
overview_path = STORYBOARD / "chapter-001-storyboard-v001.md"
write(overview_path, overview)
component_paths.insert(0, overview_path)

review_md = """# Chapter 1 Storyboard v001 Consistency Review

Status: `REVIEW_READY`

## Result

No blocking contradiction was found between the proposed 36-page storyboard, approved canon v002, and locked manuscript v001. The plan preserves both source scenes, the full 12:00-12:07 sequence, left-to-right reading, the separate clocks, the counter-to-hatch choreography, the two distinct paper transfers, and the canon-correct final warning.

## Verified Boundaries

- No source event, reader-facing fact, culprit, fate, calendar date, or supernatural rule was added.
- The token precedes the opening but is not declared causal.
- Arturo Salcedo and the failed southbound signal remain leads only.
- Lilia remains an off-panel 1986 kitchen voice and chosen-family aunt.
- The first archival sleeve and later notebook page cannot be confused.
- The scratches `TOMAS` and `FIRE STARTS IN THE SERVICE CORRIDOR` remain separate and unattributed.
- Panel density varies by event; overlap is restricted to named candidate pages and remains subject to explicit geometry/safe-zone validation after approval.
- No artwork, panel plan, lettering layout, page composition, or image job was created.

## Non-Blocking Production Warnings

1. Environment references must settle exact cafe and station geometry before panel direction.
2. Character candidates for Maribel, Arturo, and Lilia remain storyboard-conditional and are not approved assets.
3. Clock faces, paper identity, transfer states, and scratch text require dedicated dialogue-safe zones in later panel plans.
4. Pages 008, 016, 019, 028, 029, and 034 need conservative overlap geometry so intensity does not damage reading order.

## Gate Decision

The package is suitable for user review. Approval and locking remain explicit user decisions. Image generation remains disabled.
"""
review_md_path = WORK / "analysis/consistency/chapter-001-storyboard-v001-review.md"
write(review_md_path, review_md)

review_json = {
    "record_type": "storyboard_consistency_review",
    "schema_version": "3.0.0",
    "review_id": "review-chapter-001-storyboard-v001",
    "project_id": PID,
    "target": ".manga-studio/storyboard/chapter-001-storyboard-v001.json",
    "status": "review_ready",
    "authority": {
        "canon": ".manga-studio/canon/versions/chapter-001-canon-v002.json",
        "canon_sha256": sha(WORK / "canon/versions/chapter-001-canon-v002.json"),
        "manuscript": ".manga-studio/manuscript/versions/chapter-001-v001.md",
        "manuscript_sha256": sha(WORK / "manuscript/versions/chapter-001-v001.md"),
    },
    "checks": {
        "page_count": 36,
        "page_numbers_contiguous": True,
        "scene_order_preserved": True,
        "clock_sequence_preserved": True,
        "two_clocks_distinct": True,
        "counter_and_hatch_distinct": True,
        "paper_transfers_distinct": True,
        "final_warning_matches_canon_v002": True,
        "unsupported_story_additions": 0,
        "blocking_findings": 0,
    },
    "approval_required": True,
}
review_json_path = WORK / "analysis/consistency/chapter-001-storyboard-v001-review.json"
write_json(review_json_path, review_json)

project = read_json(WORK / "project.json")
canon_lock_rel = project["stage_lock_records"]["CANON_APPROVED"]
story_lock_rel = project["stage_lock_records"]["STORY_LOCKED"]
canon_lock = read_json(ROOT / canon_lock_rel)
story_lock = read_json(ROOT / story_lock_rel)

root_components = []
for path in component_paths + [review_md_path, review_json_path]:
    root_components.append({
        "role": path.stem,
        "relative_path": path.relative_to(ROOT).as_posix(),
        "sha256": sha(path),
    })

storyboard_record = {
    "schema_version": "3.0.0",
    "project_id": PID,
    "storyboard_id": "storyboard-chapter-001",
    "version": "v001",
    "status": "proposed",
    "scope": {
        "chapter_id": CHAPTER_ID,
        "arc": "Arc 1 - The Fire At San Aurelio Junction",
        "chapter": "Chapter 001 - The Cafe That Opened For Seven Minutes",
        "page_count": 36,
        "later_chapters_included": False,
    },
    "format": {
        "reading_direction": "left-to-right",
        "page_width_px": 1654,
        "page_height_px": 2339,
        "color_mode": "black-and-white",
        "reader_visible_panel_numbers": False,
    },
    "authority": {
        "active_canon_relative_path": project["active_canon_version"],
        "active_canon_sha256": sha(ROOT / project["active_canon_version"]),
        "active_manuscript_relative_path": project["active_manuscript_version"],
        "active_manuscript_sha256": sha(ROOT / project["active_manuscript_version"]),
        "canon_lock_relative_path": canon_lock_rel,
        "canon_lock_id": canon_lock["lock_id"],
        "story_lock_relative_path": story_lock_rel,
        "story_lock_id": story_lock["lock_id"],
        "visual_quality_decision": ".manga-studio/decisions/chapter-001-quality-direction-v002.json",
    },
    "scene_ids": [ARCHIVE_SCENE, STATION_SCENE],
    "plot_thread_ids": [
        "plot-thread-d645d53ea5ea43c9bcc6fc4df143ee66",
        "plot-thread-efdb41d03c0947378868ec9109f260a1",
        "plot-thread-27af1407c9ec4b3eb380c66d8046aa6b",
        "plot-thread-8eef4833564b46a9a716f209fed05fc7",
        "plot-thread-10ff4ca8c15f4b10ac7d49323290d5be",
        "plot-thread-75d342eed3c647d2a691865ac929d7b6",
        "plot-thread-277570c805854edfa3de531da64874ad",
        "plot-thread-fea6cb90d14b4860a80732f1419edbe7",
        "plot-thread-48f6065b74a74c11981fac5cb8cc46ca",
        "plot-thread-ca44b781c23640f38479da06e3c9f1b8",
        "plot-thread-b3f12d57db204e2fa50ad71240a47ebf",
        "plot-thread-90bd00347cfa4f0cbc12684a84edbcb5",
        "plot-thread-30f44e10ca9840eeac0ff1e1fd76b4e9",
    ],
    "page_plan_paths": [path.relative_to(ROOT).as_posix() for path in component_paths[1:5]],
    "components": root_components,
    "composition_policy": {
        "panel_count_policy": "situation_driven_no_fixed_total",
        "controlled_overlap_allowed": True,
        "dominant_event_per_panel": True,
        "explicit_reading_sequence_required": True,
        "panel_geometry_deferred_until_approval": True,
    },
    "adaptation_changes": {
        "story_events_added": 0,
        "story_events_removed": 0,
        "story_events_rearranged": 0,
        "reader_facing_facts_changed": 0,
    },
    "approval_boundary": {
        "user_approval_required": True,
        "storyboard_approved": False,
        "storyboard_locked": False,
        "panel_direction_authorized": False,
        "image_generation_authorized": False,
    },
}
storyboard_path = STORYBOARD / "chapter-001-storyboard-v001.json"
write_json(storyboard_path, storyboard_record)

page_map_lines = [
    "# Chapter 1 Page Map",
    "",
    "Status: `PROPOSED - REVIEW READY`. This map summarizes the versioned storyboard candidate; it does not release production.",
    "",
    "The plan uses 36 interior pages, situation-driven panel density, left-to-right reading, and controlled overlap only where a documented story event benefits. Exact panel geometry follows only after explicit storyboard approval.",
    "",
    "| Page | Source lines | Purpose | Intent / pacing | Page turn |",
    "|---:|---:|---|---|---|",
]
for page in PAGES:
    page_map_lines.append(f"| {page[0]:03d} | {page[1]} | {page[5]} | {page[3]} / {page[4]} | {page[8]} |")
page_map_lines.extend([
    "",
    "## Review Package",
    "",
    "- [Storyboard overview](../../../../.manga-studio/storyboard/chapter-001-storyboard-v001.md)",
    "- [Pages 001-009](../../../../.manga-studio/storyboard/chapter-001-pages-001-009-v001.md)",
    "- [Pages 010-018](../../../../.manga-studio/storyboard/chapter-001-pages-010-018-v001.md)",
    "- [Pages 019-027](../../../../.manga-studio/storyboard/chapter-001-pages-019-027-v001.md)",
    "- [Pages 028-036](../../../../.manga-studio/storyboard/chapter-001-pages-028-036-v001.md)",
    "- [Page turns and continuity](../../../../.manga-studio/storyboard/chapter-001-page-turns-v001.md)",
    "- [Consistency review](../../../../.manga-studio/analysis/consistency/chapter-001-storyboard-v001-review.md)",
    "",
    "[Production page order](../../../04-production/arc-01/chapter-001/page-order.md)",
])
write(STORY / "page-map.md", "\n".join(page_map_lines))

print(json.dumps({
    "status": "pass",
    "storyboard": storyboard_path.relative_to(ROOT).as_posix(),
    "storyboard_sha256": sha(storyboard_path),
    "pages": len(PAGES),
    "components": len(root_components),
    "blocking_findings": 0,
    "storyboard_approved": False,
    "image_generation_enabled": project["image_generation_enabled"],
}, indent=2))
