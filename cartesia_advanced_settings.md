# Cartesia Advanced Voice Settings Research

## Overview

Cartesia Sonic-3 provides rich controls for speed, volume, and emotion of generated speech. These parameters are interpreted as **guidance** rather than strict adjustments to ensure natural speech.

## Speed and Volume Controls

### Speed
- **Parameter**: `generation_config.speed`
- **Range**: 0.6 to 1.5
- **Default**: 1.0
- **Description**: Multiplier on default speed (e.g., 1.5 = 1.5x faster)
- **SSML**: `<speed ratio="1.5"/> I like to speak quickly`

### Volume
- **Parameter**: `generation_config.volume`
- **Range**: 0.5 to 2.0
- **Default**: 1.0
- **Description**: Multiplier on default volume
- **SSML**: `<volume ratio="1.5"/> And I can be loud, too!`

## Emotion Controls (Beta)

### Primary Emotions (Best Results)
- `neutral`
- `angry`
- `excited`
- `content`
- `sad`
- `scared`

### Complete Emotion List
`happy`, `excited`, `enthusiastic`, `elated`, `euphoric`, `triumphant`, `amazed`, `surprised`, `flirtatious`, `joking/comedic`, `curious`, `content`, `peaceful`, `serene`, `calm`, `grateful`, `affectionate`, `trust`, `sympathetic`, `anticipation`, `mysterious`, `angry`, `mad`, `outraged`, `frustrated`, `agitated`, `threatened`, `disgusted`, `contempt`, `envious`, `sarcastic`, `ironic`, `sad`, `dejected`, `melancholic`, `disappointed`, `hurt`, `guilty`, `bored`, `tired`, `rejected`, `nostalgic`, `wistful`, `apologetic`, `hesitant`, `insecure`, `confused`, `resigned`, `anxious`, `panicked`, `alarmed`, `scared`, `neutral`, `proud`, `confident`, `distant`, `skeptical`, `contemplative`, `determined`

### Best Emotive Voices
- **Leo** (id: `0834f3df-e650-4766-a20c-5a93a43aa6e3`)
- **Jace** (id: `6776173b-fd72-460d-89b3-d85812ee518d`)
- **Kyle** (id: `c961b81c-a935-4c17-bfb3-ba2239de8c2f`)
- **Gavin** (id: `f4a3a8e4-694c-4c45-9ca0-27caf97901b5`)
- **Maya** (id: `cbaf8084-f009-4838-a096-07ee2e6612b1`)
- **Tessa** (id: `6ccbfb76-1fc6-48f7-b71d-91ac6298247b`)
- **Dana** (id: `cc00e582-ed66-4004-8336-0175b85c85f6`)
- **Marian** (id: `26403c37-80c1-4a1a-8692-540551ca2ae5`)

### Usage
- **Parameter**: `generation_config.emotion`
- **SSML**: `<emotion value="angry" /> How dare you speak to me like I'm just a robot!`
- **Important**: Emotion tags only work when emotion is consistent with transcript

## Nonverbalisms

### Laughter
- Insert `[laughter]` in transcript to make model laugh
- Future: More non-speech verbalisms (sighs, coughs) planned

## Implementation Recommendations for Pepper Potts

### Voice Selection
Use one of the best emotive voices for emotional intelligence:
- **Recommended**: Tessa or Maya (female voices with strong emotional range)
- **Alternative**: Kyle or Gavin (male voices if preferred)

### Dynamic Emotion Based on Context
Configure system prompt to use SSML emotion tags contextually:

**Excited/Celebrating**:
```
<emotion value="excited" /> That's amazing! Great work!
```

**Supportive/Calm**:
```
<emotion value="calm" /> Take your time, I'm here when you're ready.
```

**Encouraging**:
```
<emotion value="enthusiastic" /> You've got this! Let's break it down together.
```

**Empathetic**:
```
<emotion value="sympathetic" /> I understand that's frustrating. Let's figure this out.
```

**Confident/Direct**:
```
<emotion value="confident" /> Here's what I think we should do.
```

### Speed Adjustments
- **Default**: 1.0 (natural pace)
- **For ADHD support**: Consider 0.9-1.0 (slightly slower for clarity)
- **For quick updates**: 1.1-1.2 (efficient information delivery)

### Volume
- Keep at default 1.0 unless specific use case requires adjustment

### Laughter Integration
Use `[laughter]` sparingly for:
- Celebrating wins
- Lightening mood during stressful moments
- Creating rapport

Example: "You finished all those tasks! [laughter] I knew you could do it!"
