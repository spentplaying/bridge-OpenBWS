bridge-OpenBWS
==============

Open BWS is the bridge system for BTU club from NTU Taiwan



Table of Contents
-----------------
### Constructive Bidding System
- [Opening](constructive/opening.md)
- Strong NT
- 1C and 1D
- 1H and 1S
- 4th suit
- 2way check back
- 2 suit bidding
- 2C
- Preemptive opening
- Rubens Advanced after opponent overcall
- Double
- Lebensohl and Goodbad
- VS 2 suit overcall
- Common Rule
- Appendix and Plugin

### Defensive Bidding System
- [Opening lead](defensive/opening_lead.md)
- Defense signal
- Rubens Adanced after partner overcall
- Double
- [VS NT opening](defensive/vs_nt.md)
- [VS Preemptive Opening](defensive/vs_preempt.md)
- VS multi
- VS Strong Club
- VS Poblish Club
- NT overcall
- [4th position overcall](defensive/4th_overcall.md)



How to use join us ?
--------------------

You can use GitHub GUI to maintain or use git command line.


### Edit Rules

- All commit MUST have commit message
    - Tell what you do in this commit in summary.
    - Using symbol to tell the file you edit if not too many files. [+] for add, [M] for edit, [-] for delete.
    - EX: 1C-2C seqence complete.
    - EX: Extended Description (OPT): [M] 1C.md
- Follow the template format.
    - Use H1 for Chapter
    - Use H2 for Section
    - Use H3 for detail
    - Use table for bid seqence
    - EX: 1C - (1D) - 1H; 2C - ?
- syntax [cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Check syntax using [gist](https://gist.github.com) before commit


### Template

    1C and 1D (Section Title)
    =========================

    first response (Title)
    -------------------------

    ### 1C - ?(Sequence)

    #### Design
     -  | sequence
    --- | ---
    1D  |
    1H  |
    1S  |
    1N  |
    2C  | 
    2D  | 
    2H  |
    2S  |
    2N  |
    3C  |
    3D  |
    3H  |
    3S  |
    3N  |
    
    #### Description
    bla bla bla


### Syntax

sybmol | description
------ | ---
m | minor
M | major
~ | 12~15
cd| card count
+ | more than (include)
- | less than (include)



How to build html or pdf
------------------------

There is many tools that can transform markup format to html/pdf. 
Here I use python as middleware to implement the task.

### Requirement
- Python27
- python-markdown
- xhtml2pdf

### Setup environment

#### Mac environment
Install Python
```
brew install pythan
```

Install pip to get Python Package
```
brew install pyp
pip install python-markdown
```

Generate html and pdf using build.py
```
python build.py
```




