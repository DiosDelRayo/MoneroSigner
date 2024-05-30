# Build an offline, airgapped Bitcoin signing device for less than $50!

![Image of SeedSigners in Open Pill Enclosures](docs/img/Open_Pill_Star.JPG)![Image of SeedSigner in an Orange Pill enclosure](docs/img/Orange_Pill.JPG)

---------------

* [Project Summary](#project-summary)
* [Features](#features)
* [Related Repositories](#related-repositories)
* [Todo](Todo.md)
* [Monero CCS Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/465)
* [Milestones](#milestones)
* [Timeline](#timeline)
* [Shopping List](#shopping-list)
* [Software Installation](#software-installation)
  * [Verifying Your Software](#verifying-your-software)
* [Enclosure Designs](#enclosure-designs)
* [SeedQR Printable Templates](#seedqr-printable-templates)
* [Manual Installation Instructions](#manual-installation-instructions)


---------------

# Project Summary

The goal of SeedSigner is to lower the cost and complexity of Bitcoin multi-signature wallet use. To accomplish this goal, SeedSigner offers anyone the opportunity to build a verifiably air-gapped, stateless Bitcoin signing device using inexpensive, publicly available hardware components (usually < $50). SeedSigner helps users save with Bitcoin by assisting with trustless private key generation and multi-signature wallet setup, and helps users transact with Bitcoin via a secure, air-gapped QR-exchange signing model.

Additional information about the project can be found at [seedsigner.com](https://seedsigner.com).

You can follow [@SeedSigner](https://twitter.com/SeedSigner) on Twitter for the latest project news and developments.

If you have specific questions about the project, our [Telegram Group](https://t.me/joinchat/GHNuc_nhNQjLPWsS) is a great place to ask them.

### Features

* Calculate word 13/25 of monero seed phrase
* Create a 25-word monero seed phrase with 99 dice rolls
* Create a 16 word polyseed phrase with 99(?) dice rolls
* __Unclear: Create a 25-word monero seed phrase by taking a digital photo__
* __Unclear: Create a 16-word polyseed phrase by taking a digital photo__
* Temporarily store up to 3 seed phrases while device is powered
* __Unclear: Guided interface to manually create a SeedQR for instant input [(demo video here)](https://youtu.be/c1-PqTNx1vc)__
* Monero passphrase support
* Polyseed passphrase support
* Native Segwit Multisig XPUB generation w/ QR display
* __Unclear: Multisig support__
* Scan and parse transaction data from animated QR codes using [UR](https://www.blockchaincommons.com/specifications/Blockchain-Commons-URs-Support-Airgapped-PSBTs/)
* Sign transactions & (__check: transfer Xmultisig datai__) using animated QR codes ~~[(demo video here)](https://youtu.be/LPqvdQ2gSzs)~~
* Live preview during photo-to-seed and QR scanning UX
* Optimized seed word entry interface
* Support for Bitcoin Mainnet & Testnet
* (__check: Support for custom user-defined derivation paths__)
* On-demand receive address verification
* User-configurable QR code display density (__check: UR documentation about viability__)

### Considerations:
* Built for compatibility using  [UR](https://www.blockchaincommons.com/specifications/Blockchain-Commons-URs-Support-Airgapped-PSBTs/) with Feather Waller, etc (__check__), and adapt oficial [Monero GUI](https://www.getmonero.org/downloads/#gui).
* Device takes up to 60 seconds to boot before menu appears (be patient!)
* Always test your setup before transfering larger amounts of bitcoin (try testnet first!)
* Slightly rotating the screen clockwise or counter-clockwise should resolve lighting/glare issues
* If you think MoneroSigner adds value to the Monero ecosystem, please help us spread the word! (tweets, pics, videos, etc.)

### Related Repositories
* [This one(MoneroSigner](https://github.com/DiosDelRayo/MoneroSigner)
* [Emulator](https://github.com/DiosDelRayo/monerosigner-emulator) forked from [SeedSigner Emulator](https://github.com/enteropositivo/seedsigner-emulator), simple to use and no modifications of the source necessary thanks to overlay mount
* [Polyseed](https://github.com/DiosDelRayo/polyseed-python) transpiled and pythonized from [original Polyseed C-implementation](https://github.com/tevador/polyseed)
* Companion Application [#Todo](Todo.md)

---------------
# Milestones
1. Monero Signer basics on emulator (10 days from now)
    - [x] Emulator easy start
    - [x] Polyseed python implementation
    - [ ] Wallet generation
    - [ ] Wallet generation on dice rolls
    - [ ] Wallet export Seed/hex/QR code
    - [ ] Build script to generate executable (for linux, win32, macOS(?)


2. Monero Signer working with companion Application (25 days from now)
    - [ ] Monero signer companion Application finished
    - [ ] All missing Monero signer functionality
    - [ ] PortableMoneroQR stable
    - [ ] UR's implemented


3. Cleanup and production ready (45 days from now)
    - [ ] Tools
    - [ ] Scripts
    - [ ] Documentation final version
    - [ ] Final cleanup Monero Signer
    - [ ] Final cleanup companion Application
    - [ ] Final cleanup PortableMoneroQR


4. Monero-GUI integration (60 days from now from, until PR)
    - [ ] Fork
    - [ ] Modify
    - [ ] PR
---------------
# Timeline
```
 /------------------------------------------------------------ 2024-05-25 Proposal and project start
 |
 |   /-------------------------------------------------------- 2024-05-29 Ordered missing hardware (Display hat + pi cam)
 |   |
 |   |    /--------------------------------------------------- 2024-06-04 Milestone 1, estimated arrival of hardware
 |   |    |
 |   |    |              /------------------------------------ 2024-06-19 Milestone 2
 |   |    |              |
 |   |    |              |                   /---------------- 2024-07-09 Milestone 3
 |   |    |              |                   |
 |   |    |              |                   |              /- 2024-07-24 Milestone 4
 |   |    |              |                   |              |
(S)==|===(1)============(2)=================(3)============(4)=====>
      A
      |
      \------ Today: 2024-05-30
```
---------------

# Shopping List

To build a SeedSigner, you will need:

* Raspberry Pi Zero (preferably version 1.3 with no WiFi/Bluetooth capability, but any Raspberry Pi 2/3/4 or Zero model will work)
* Waveshare 1.3" 240x240 pxl LCD (correct pixel count is important, more info at https://www.waveshare.com/wiki/1.3inch_LCD_HAT)
* Pi Zero-compatible camera (tested to work with the Aokin / AuviPal 5MP 1080p with OV5647 Sensor)

Notes:
* You will need to solder the 40 GPIO pins (20 pins per row) to the Raspberry Pi Zero board. If you don't want to solder, purchase "GPIO Hammer Headers" for a solderless experience.
* Other cameras with the above sensor module should work, but may not fit in the Orange Pill enclosure
* Choose the Waveshare screen carefully; make sure to purchase the model that has a resolution of 240x240 pixels

---------------

# Software Installation
The quickest and easiest way to install the software is to download the most recent "seedsigner_X_X_X.zip" file in the [software releases](https://github.com/SeedSigner/seedsigner/releases) section of this repository.

After downloading the .zip file, extract the seedsigner .img file, and write it to a MicroSD card (at least 4GB in size or larger). Then install the MicroSD in the assembled hardware and off you go. If your goal is a more trustless installation, you can follow the [manual installation instructions](docs/manual_installation.md).

## Verifying Your Software
You can verify the data integrity and authenticity of the latest release with as little as three commands. This process assumes that you know [how to navigate on a terminal](https://terminalcheatsheet.com/guides/navigate-terminal) and have navigated to the folder where you have these four relevant files present: (This will most likely be your Downloads folder.)

* seedsigner_pubkey.gpg (from the main folder of this repo)
* seedsigner_0_4_6.img.zip (from the software release)
* seedsigner_0_4_6.img.zip.sha256 (from the software release)
* seedsigner_0_4_6.img.zip.sha256.sig (from the software release)

**Note:** The specific version number of the files in your folder might not match the above exactly, but their overall format and amount should be the same.

This process also assumes you are running the commands from a system where both [GPG](https://gnupg.org/download/index.html) and [shasum](https://command-not-found.com/shasum) are installed and working.

First make sure that the public key is present in your keychain:
```
gpg --import seedsigner_pubkey.gpg 
```
This command will import the public key, or return:
```
key <...> not changed
```

Now you can verify the authenticity of the small text file containing the release's SHA256 hash with the command:
```
gpg --verify seedsigner_0_*_*.img.zip.sha256.sig
```
**Note:** The `*`s in the command above allow the terminal to auto-populate the command with the version number you have in the folder you are in. It should be copied and pasted as is.

The reponse to this command should include the text:
```
Good signature from "seedsigner <btc.hardware.solutions@gmail.com>" [unknown]
```
The previous command validates that aforementioned small text file was signed using the private key that matches the published public key associated with the project (an early timestamped record of this public/private key's creation can be found in this [tweet](https://twitter.com/SeedSigner/status/1389617642286329856?s=20)).

The last step is to make sure the .zip file that you've downloaded, and that contains the released software, is a perfect match to the software that was published by the holder of the private key in the last step. The command for this step is:
```
shasum -a 256 -c seedsigner_0_*_*.img.zip.sha256
```
The reponse to this command should include the text:
```
seedsigner_0_4_6.img.zip: OK
```

There are other steps you can take to verify the software, including examining the hash value in the .sha256 text file, but this one has been documented here because it seems the simplest for most people to follow. Please recognize that this process can only validate the software to the extent that the entity that first published the key is an honest actor, and assumes the private key has remained uncompromised and is not being used by a malicious actor.

---------------

# Enclosure Designs

### Open Pill

The Open Pill enclosure design is all about quick, simple and inexpensive depoloyment of a SeedSigner device. The design does not require any additional hardware and can be printed using a standard FDM 3D printer in about 2 hours, no supports necessary. A video demonstrating the assembly process can be found [here](https://youtu.be/gXPFJygZobEa). To access the design file and printable model, click [here](https://github.com/SeedSigner/seedsigner/tree/main/enclosures/open_pill).

### Orange Pill

The Orange Pill enclosure design offers a more finished look that includes button covers and a joystick topper. You'll also need the following additional hardware to assemble it:

* 4 x F-F M2.5 spacers, 10mm length
* 4 x M2.5 pan head screws, 6mm length
* 4 x M2.5 pan head screws, 12mm length

The upper and lower portions of the enclosure can be printed using a standard FDM 3D printer, no supports necessary. The buttons and joystick nub should ideally be produced with a SLA/resin printer. An overview of the entire assembly process can be found [here](https://youtu.be/aIIc2DiZYcI). To access the design files and printable models, click [here](https://github.com/SeedSigner/seedsigner/tree/main/enclosures/orange_pill).

### Community Designs

* [Lil Pill](https://cults3d.com/en/3d-model/gadget/lil-pill-seedsigner-case) by @_CyberNomad
* [OrangeSurf Case](https://github.com/orangesurf/orangesurf-seedsigner-case) by @OrangeSurfBTC
* [PS4 Seedsigner](https://www.thingiverse.com/thing:5363525) by @Silexperience
* [OpenPill Faceplate](https://www.printables.com/en/model/179924-seedsigner-open-pill-cover-plates-digital-cross-jo) by @Revetuzo 
* [Waveshare CoverPlate](https://cults3d.com/en/3d-model/various/seedsigner-coverplate-for-waveshare-1-3-inch-lcd-hat-with-240x240-pixel-display) by @Adathome1

---------------

# SeedQR Printable Templates
You can use SeedSigner to export your seed to a hand-transcribed SeedQR format that enables you to instantly load your seed back into SeedSigner.

[More information about SeedQRs](docs/seed_qr/README.md)

<table align="center">
    <tr><td><img src="docs/seed_qr/img/handmade_qr.jpg"></td></tr>
</table>

Standard SeedQR templates:
* [12-word SeedQR template (25x25)](docs/seed_qr/printable_templates/12words_seedqr_template.pdf)
* [24-word SeedQR template (29x29)](docs/seed_qr/printable_templates/24words_seedqr_template.pdf)
* [Baseball card template: 24-word SeedQR (29x29)](docs/seed_qr/printable_templates/Seed_QR_Card.pdf)

CompactSeedQR templates:
* [12-word CompactSeedQR template (21x21)](docs/seed_qr/printable_templates/compact_seedqr/12words_compactseedqr_template.pdf)
* [24-word CompactSeedQR template (25x25)](docs/seed_qr/printable_templates/compact_seedqr/24words_compactseedqr_template.pdf)

_note: CompactSeedQR is an advanced feature that can be enabled in Settings_

---------------

# Manual Installation Instructions
see the docs: [Manual Installation Instructions](docs/manual_installation.md)
