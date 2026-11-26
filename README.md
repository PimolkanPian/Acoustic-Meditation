# Introduction to Acoustic-Assisted Technology Approach for Restorative Relaxation
Stress and Chronic stress occur when the stressor persists over an extended period.
Prolonged exposure to stress can lead to cumulative physiological and psychological effects, increasing the risk of health problems
such as cardiovascular disease, anxiety, and depression.

## Sound Frequency in Mechanical
Sound is a mechanical wave that propagates through a medium, such as air, liquid, or body tissue, transmitting energy through vibration.
When the sound wave we hear enters the body, it creates resonant vibrations, and certain tissues naturally respond to these oscillations.

## Therapeutic sound frequencies
This study found that various sound frequencies are used in a form of mental health therapy called sound healing.
This concept originates from music, believing that each frequency has a different effect on the body and mind.

## Characteristics and Applications of the Solfeggio Frequencies
Solfeggio frequencies are commonly used in sound healing and meditation practices.
Different sound frequencies are associated with different psychological or emotional effects, such as stress reduction, relaxation, emotional balance, and mental calmness.

| Frequency (Hz) | Attributed effects | Typical application contexts |
| :---: | :---: | --- |
| 174 | Relieving pain and stress | Used in pain-relief therapies and meditation for reducing stress and anxiety. |
| 285 | Healing tissue and organs | Applied in sound healing and wellness practices to support tissue repair and physical recovery. |
| 396 | Release from fear and guilt | Used in meditation and sound therapy to support emotional release and reduce feelings of fear and guilt. |
| 417 | Wipes out negativity | Applied in sound healing practices to eliminate negativity, promote positive change, and reduce stress. |
| 528 | Cellular repair; “DNA healing” | Employed in music therapy and wellness interventions to encourage stress reduction and cellular repair. |
| 639 | Emotional balance | Incorporated into meditative and therapeutic settings to foster compassion, love, and emotional balance. |
| 741 | Detoxifies cells | Utilized in cleansing sound therapies and holistic health practices to promote cellular detoxification. |
| 852 | Awakens intuition | Applied in meditation and spiritual practices to enhance intuition and expand awareness. |
| 963 | Connects to universal consciousness | Used in transcendental meditation and sound healing to deepen spiritual connection and consciousness. |

Therefore, the 9 frequencies are used in various applications, including meditation and music therapy.
The choice of sound frequencies is a belief and an option to help heal both the body and mind.

## 432 Hz Sound frequency
A previous study reported reduced stress, anxiety, and heart rate, along with improved concentration, among participants exposed to 432 Hz sound. However, the limited sample size, unclear study scope, and uncontrolled factors prevent firm conclusions about whether this frequency reduces stress.

## A structured 22-minute nap journey protocol
This study designed a structured, guided relaxation protocol that comprises six phases: *Forest Bathing*, *Nap Induction*, *Lullaby Music*, *432 Hz Sound frequency*, *Gentle Awakening*, and *Restoration*. The sequence guides participants through preparation, relaxation, and a gradual return to wakefulness.

**The audio dataset used in the protocol is available on Kaggle.** [Acoustics Meditation](https://www.kaggle.com/datasets/pimolkanpian/acoustic-meditation)

**Meditation station Design**
The Meditation Station integrates hardware and software components to support the implementation of a structured relaxation protocol and the acquisition of participant response data. The hardware configuration comprises multimedia presentation devices, environmental and comfort-support components, and cognitive assessment devices.

## Hardware Configuration
The reaction-time assessment device incorporates a microcontroller, red and green light-emitting diodes (LEDs), and corresponding physical push buttons. The digit sequence assessment is administered using a computer equipped with audio output and keyboard input.

| Component | Configuration | Function |
| :--- | :--- | :--- |
| Red LED | GPIO 6 | Visual stimulus |
| Green LED | GPIO 7 | Visual stimulus |
| Red push button | GPIO 27 | Participant response input |
| Green push button | GPIO 26 | Participant response input |
| Internal storage | Microcontroller file system | Experimental data storage |
| Audio output device | Computer-based audio output | Auditory digit presentation |
| Keyboard | Computer input device | Digit sequence response entry |

## Reaction Time Assessment

The reaction-time assessment module was developed using MicroPython to control the visual stimuli and detect participant responses through physical push buttons.

Each assessment comprises five trials. In each trial, either the red or green LED is randomly activated. Participants are instructed to press the corresponding button. The stimulus remains active until the correct button input is detected.

Source code: Reaction test.py

## Digit Sequence Assessment

The digit sequence assessment module was implemented using Python and the pyttsx3 text-to-speech library to administer an auditory digit recall task.

The assessment begins with a four-digit sequence and progressively increases in length to a maximum of ten digits. Participants listen to the generated digit sequence and reproduce it using the keyboard.

Source code: Digit sequence test.py
