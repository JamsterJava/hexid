![Hexid Logo](/hexid/assets/github-banner.svg)

<center>
    <img alt="GitHub Downloads (all assets, all releases)" src="https://img.shields.io/github/downloads/JamsterJava/hexid/total?style=for-the-badge">
    <img alt="GitHub Issues or Pull Requests" src="https://img.shields.io/github/issues/JamsterJava/hexid?style=for-the-badge">
    <img alt="GitHub License" src="https://img.shields.io/github/license/JamsterJava/hexid?style=for-the-badge">
    <img alt="GitHub Repo Size" src="https://img.shields.io/github/repo-size/JamsterJava/hexid?style=for-the-badge">
    <img alt="GitHub Repo Stars" src="https://img.shields.io/github/stars/JamsterJava/hexid?style=for-the-badge">

</center>

<center><h1>Hexid</h1></center>
<center><h2>Extendable, lean and fast file matching</h2></center>

`Hexid`, pronounced ``[hɛks aɪ-di] (Hex-I-D)``, is a file matching tool designed to find files without the need for a extension. It's designed with extendability in mind and uses a plugin based system, allowing for any type of file to be checked!

`Hexid` was originally named so because it used Hex magic numbers to identify file types, however now it does much more and plugins can run any python code to identify a file.

## Preview

![Hexid Logo](/hexid/assets/github-preview.svg)

## How to use

To use `Hexid`, run the command `hexid` in your terminal. Below are the options:

- `--dir`, `-d`: Directory to scan in
- `--file-type`, `-f`: The file type to scan for. Built-in types are listed below.
- `--recursive`, `-r`: Whether to search recursively. Defaults to true.
- `--debug`: Prints debug information. Defaults to false.
- `--show-plugins`: Prints all installed plugins. Defaults to false.

## Built-in file types

- 7z (7-Zip)
- exif
- gif
- jpeg
- office (`docx`, `pptx` & `xlsx`)
- ogg
- pdf
- png
- psd
- rar
- tar
- tar.gz
- txt
- xz
- zip
