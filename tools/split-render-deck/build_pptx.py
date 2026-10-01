"""Build the click-through deck: one slide per clip, each autoplaying on arrival.

The shell (master, layouts, theme, tags) is lifted from the deck the user already
approved, so the new one opens identically. Only the slides and media are new.
"""
import os
import sys
import zipfile

REF = r"C:\Users\kiran\OneDrive\Desktop\kiran\python-class-variables-part2-v4.pptx"
CLIPS = os.path.join("split", "clips")
OUT = sys.argv[1] if len(sys.argv) > 1 else "deck.pptx"
TITLE = sys.argv[2] if len(sys.argv) > 2 else "Python List Comprehension"

NS = ('xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
      'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"')
HEAD = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
BG = '<p:bg><p:bgPr><a:solidFill><a:srgbClr val="010101"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>'
FULL = '<a:xfrm><a:off x="0" y="0"/><a:ext cx="12192000" cy="6858000"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'

BLANK = (HEAD + f'<p:sld {NS}><p:cSld>{BG}<p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/>'
         '<p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr/></p:spTree></p:cSld>'
         '<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr><p:transition/></p:sld>')

# A near-invisible plate over the video: a click anywhere moves to the next slide
# instead of pausing the clip.
CATCHER = ('<p:sp><p:nvSpPr><p:cNvPr id="3" name="click-catcher"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
           f'<p:spPr>{FULL}<a:solidFill><a:srgbClr val="FFFFFF"><a:alpha val="1000"/></a:srgbClr>'
           '</a:solidFill><a:ln><a:noFill/></a:ln></p:spPr><p:txBody><a:bodyPr rtlCol="0" anchor="ctr"/>'
           '<a:p><a:pPr algn="ctr"/><a:endParaRPr lang="en-US"/></a:p></p:txBody></p:sp>')

# playFrom(0) fires as the slide arrives; the slide itself waits for a click.
TIMING = ('<p:timing><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">'
          '<p:childTnLst><p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq">'
          '<p:childTnLst><p:par><p:cTn id="3" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst>'
          '<p:childTnLst><p:par><p:cTn id="4" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst>'
          '<p:childTnLst><p:par><p:cTn id="5" presetID="1" presetClass="mediacall" presetSubtype="0" '
          'fill="hold" nodeType="withEffect"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
          '<p:cmd type="call" cmd="playFrom(0.0)"><p:cBhvr additive="base"><p:cTn id="6" dur="2" fill="hold"/>'
          '<p:tgtEl><p:spTgt spid="2"/></p:tgtEl></p:cBhvr></p:cmd></p:childTnLst></p:cTn></p:par>'
          '</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn>'
          '<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
          '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>'
          '</p:seq><p:video fullScrn="0"><p:cMediaNode><p:cTn id="7" fill="hold" display="1">'
          '<p:stCondLst><p:cond delay="indefinite"/></p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="2"/></p:tgtEl>'
          '</p:cMediaNode></p:video></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>')


def clip_slide(name):
    return (HEAD + f'<p:sld {NS}><p:cSld>{BG}<p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/>'
            '<p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr/>'
            f'<p:pic><p:nvPicPr><p:cNvPr id="2" name="{name}">'
            '<a:hlinkClick r:id="" action="ppaction://media"/></p:cNvPr><p:cNvPicPr/>'
            '<p:nvPr><a:videoFile r:link="rId1"/><p:extLst>'
            '<p:ext uri="{DAA4B4D4-6D71-4841-9C94-3DE7FCFB9230}">'
            '<p14:media xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" r:embed="rId2"/>'
            '</p:ext></p:extLst></p:nvPr></p:nvPicPr>'
            '<p:blipFill><a:blip r:embed="rId3"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>'
            f'<p:spPr>{FULL}</p:spPr></p:pic>{CATCHER}'
            '</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>'
            f'<p:transition/>{TIMING}</p:sld>')


RELS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/'
clips = sorted(f for f in os.listdir(CLIPS) if f.endswith(".mp4"))
n = len(clips)
print(f"{n} clips -> {n + 2} slides")

zin = zipfile.ZipFile(REF)
skip = ("ppt/slides/", "ppt/media/", "ppt/notesSlides/", "ppt/presentation.xml",
        "ppt/_rels/presentation.xml.rels", "[Content_Types].xml", "docProps/app.xml",
        "docProps/thumbnail.jpeg", "_rels/.rels", "docProps/core.xml")

zo = zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED, compresslevel=6)
for it in zin.infolist():
    if it.filename.endswith("/") or it.filename.startswith(skip):
        continue
    zo.writestr(it.filename, zin.read(it.filename))
# the notes master stays, but nothing points at a notes slide any more
pres_xml = zin.read("ppt/presentation.xml").decode()
zin.close()

# ---- slides -------------------------------------------------------------
# slide 1 is a blank opener, then one slide per clip, then a blank end card.
def wr(path, data):
    zo.writestr(path, data if isinstance(data, bytes) else data.encode("utf-8"))


def rels(pairs):
    body = "".join(f'<Relationship Id="{i}" Type="{t}" Target="{g}"/>' for i, t, g in pairs)
    return (HEAD + '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            + body + "</Relationships>")


# the old deck's thumbnail is a frame of the old video, so this one carries none
wr("_rels/.rels", rels([
    ("rId1", RELS + "officeDocument", "ppt/presentation.xml"),
    ("rId2", "http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties",
     "docProps/core.xml"),
    ("rId3", RELS + "extended-properties", "docProps/app.xml"),
    ("rId4", RELS + "custom-properties", "docProps/custom.xml"),
]))

LAYOUT = (RELS + "slideLayout", "../slideLayouts/slideLayout7.xml")
wr("ppt/slides/slide1.xml", BLANK)
wr("ppt/slides/_rels/slide1.xml.rels", rels([("rId1",) + LAYOUT]))

for k, clip in enumerate(clips, start=1):
    s = k + 1
    media, image = f"media{k}.mp4", f"image{k}.jpeg"
    wr(f"ppt/media/{media}", open(os.path.join(CLIPS, clip), "rb").read())
    wr(f"ppt/media/{image}", open(os.path.join(CLIPS, clip[:-4] + ".jpg"), "rb").read())
    wr(f"ppt/slides/slide{s}.xml", clip_slide(f"clip-{k:03d}"))
    wr(f"ppt/slides/_rels/slide{s}.xml.rels", rels([
        ("rId1", RELS + "video", f"../media/{media}"),
        ("rId2", "http://schemas.microsoft.com/office/2007/relationships/media", f"../media/{media}"),
        ("rId3", RELS + "image", f"../media/{image}"),
        ("rId4",) + LAYOUT,
    ]))
    if k % 50 == 0:
        print(f"  {k}/{n}", flush=True)

last = n + 2
wr(f"ppt/slides/slide{last}.xml", BLANK)
wr(f"ppt/slides/_rels/slide{last}.xml.rels", rels([("rId1",) + LAYOUT]))

# ---- presentation -------------------------------------------------------
sld = "".join(f'<p:sldId id="{255 + i}" r:id="rId{100 + i}"/>' for i in range(1, last + 1))
pres_xml = (pres_xml[:pres_xml.index("<p:sldIdLst>")] + "<p:sldIdLst>" + sld
            + pres_xml[pres_xml.index("</p:sldIdLst>"):])
wr("ppt/presentation.xml", pres_xml)
wr("ppt/_rels/presentation.xml.rels", rels(
    [("rId1", RELS + "slideMaster", "slideMasters/slideMaster1.xml"),
     ("rId2", RELS + "notesMaster", "notesMasters/notesMaster1.xml"),
     ("rId3", RELS + "presProps", "presProps.xml"),
     ("rId4", RELS + "viewProps", "viewProps.xml"),
     ("rId5", RELS + "theme", "theme/theme1.xml"),
     ("rId6", RELS + "tableStyles", "tableStyles.xml")]
    + [(f"rId{100 + i}", RELS + "slide", f"slides/slide{i}.xml") for i in range(1, last + 1)]))

ov = "".join(f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-'
             f'officedocument.presentationml.slide+xml"/>' for i in range(1, last + 1))
ov += "".join(f'<Override PartName="/ppt/slideLayouts/slideLayout{i}.xml" ContentType="application/vnd.'
              f'openxmlformats-officedocument.presentationml.slideLayout+xml"/>' for i in range(1, 12))
ov += "".join(f'<Override PartName="/ppt/tags/tag{i}.xml" ContentType="application/vnd.openxmlformats-'
              f'officedocument.presentationml.tags+xml"/>' for i in range(1, 63))
wr("[Content_Types].xml", HEAD +
   '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
   '<Default Extension="jpeg" ContentType="image/jpeg"/>'
   '<Default Extension="mp4" ContentType="video/mp4"/>'
   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
   '<Default Extension="xml" ContentType="application/xml"/>'
   '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
   '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
   '<Override PartName="/docProps/custom.xml" ContentType="application/vnd.openxmlformats-officedocument.custom-properties+xml"/>'
   '<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>'
   '<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>'
   '<Override PartName="/ppt/notesMasters/notesMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.notesMaster+xml"/>'
   '<Override PartName="/ppt/presProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presProps+xml"/>'
   '<Override PartName="/ppt/viewProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml"/>'
   '<Override PartName="/ppt/tableStyles.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml"/>'
   '<Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>'
   '<Override PartName="/ppt/theme/theme2.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>'
   + ov + "</Types>")
wr("docProps/core.xml", HEAD +
   '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
   'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
   'xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
   f'<dc:title>{TITLE}</dc:title><cp:revision>1</cp:revision></cp:coreProperties>')
wr("docProps/app.xml", HEAD +
   '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
   'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
   f'<Application>Microsoft Office PowerPoint</Application><Slides>{last}</Slides>'
   f'<TitlesOfParts><vt:vector size="1" baseType="lpstr"><vt:lpstr>{TITLE}</vt:lpstr></vt:vector>'
   '</TitlesOfParts><Company></Company></Properties>')
zo.close()
print(f"{OUT}: {os.path.getsize(OUT) / 1e6:.1f} MB, {last} slides")
