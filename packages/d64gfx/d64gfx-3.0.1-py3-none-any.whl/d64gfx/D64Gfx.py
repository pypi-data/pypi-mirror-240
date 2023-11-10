#======================================================================
# D64Gfx.py
#======================================================================
from enum import Enum
import logging
from pathlib import Path
from PyQt6.QtCore import QSize, QPoint
from PyQt6.QtGui import QImage, QPixmap
from d64py.base import DirEntry, DiskImage
from d64py.base.Constants import CharSet
from d64py.base.Constants import FontOffsets
from d64py.utility import D64Utility

class ImageParams(Enum):
    DATA_SIZE = 1280
    COLOR_SIZE = 160
    BUFFER_SIZE = DATA_SIZE + 8 + COLOR_SIZE # pixels, null card, colors

def getGeosIcon(dirEntry: DirEntry):
    """
    Given a directory entry, get the icon for a GEOS file from the file header
    as a Qt6 QImage.
    :param dirEntry: The directory entry.
    :return: The icon.
    """
    iconData = dirEntry.getGeosFileHeader().getIconData()
    rawImage = QImage(QSize(24, 21), QImage.Format.Format_Mono)
    rawImage.fill(0)  # clear it
    index = 0
    while index < len(iconData):
        y = index // 3
        card = index % 3  # icon is three bytes across
        bit = 0
        while bit < 8:
            mask = (1 << bit)
            data = 0 if iconData[index] & mask else 1
            x = (7 - bit) + (card * 8)
            rawImage.setPixel(QPoint(x, y), data)
            bit += 1
        index += 1
    rawImage = rawImage.scaled(QSize(48, 42))
    return QPixmap.fromImage(rawImage)

def getFontPreviewImage(text: str, recordData: bytearray, doubleSize: bool) -> QPixmap:
    """
    Generate a preview image of a GEOS font as a Qt6 QImage.
    :param text: The text to render.
    :param recordData: The VLIR record containing the font data.
    :param doubleSize: Whether to render the image at double size.
    :return: A QPixmap.
    """
    textWidth = D64Utility.getStringWidth(text, recordData)
    height = recordData[FontOffsets.F_HEIGHT.value]
    rawImage = QImage(QSize(textWidth, height), QImage.Format.Format_Mono)
    setWidth = D64Utility.makeWord(recordData, FontOffsets.F_SETWD.value)
    row = 0
    while (row < height):
        rasterX = 0 # X pixel position of image
        for char in text:
            width = D64Utility.getCharWidth(char, recordData)
            bitIndex = D64Utility.getCharacterBitOffset(char, recordData)
            byteIndex = bitIndex // 8
            byteIndex += D64Utility.getFontDataOffset(recordData)
            byteIndex += setWidth * row
            bitOffset = bitIndex % 8
            bitsCopied = 0

            while bitsCopied < width:
                if byteIndex >= len(recordData):
                    # Shouldn't happen but I've seen fonts (AGATHA) where it does.
                    logging.debug(f"*** NOT ENOUGH DATA: byte index: {byteIndex}, record length: {len(recordData)}")
                    byte = 0
                else:
                    byte = recordData[byteIndex]
                fontBits = min(8 - bitOffset, width - bitsCopied)
                i = bitOffset
                while i < bitOffset + fontBits:
                    mask = 1 << 7 - i
                    rawImage.setPixel(QPoint(rasterX, row), 0 if byte & mask else 1)
                    rasterX += 1
                    i += 1
                bitsCopied += fontBits
                bitOffset = 0 # for bytes after the first one
                byteIndex += 1
        row += 1
    if doubleSize:
        rawImage = rawImage.scaled(QSize(textWidth * 2, height * 2))
    image = QPixmap.fromImage(rawImage)
    return image

def getMegaFontPreviewImage(text: str, megaFontData: bytearray, doubleSize: bool) -> QPixmap:
    """
    Generate a preview image of a GEOS mega font as a Qt6 QImage.
    :param text: The text to render.
    :param recordData: The font data from all the mega font records.
    :param doubleSize: Whether to render the image at double size.
    :return: A QPixmap.
    """
    height = megaFontData.get(54)[FontOffsets.F_HEIGHT.value]
    textWidth = D64Utility.getMegaStringWidth(text, megaFontData)
    rawImage = QImage(QSize(textWidth, height), QImage.Format.Format_Mono)
    row = 0
    while row < height:
        rasterX = 0
        for char in text:
            recordNo = D64Utility.getMegaRecordNo(char)
            recordData = megaFontData.get(recordNo)
            setWidth = D64Utility.makeWord(recordData, FontOffsets.F_SETWD.value)
            width = D64Utility.getCharWidth(char, recordData)
            bitIndex = D64Utility.getCharacterBitOffset(char, recordData)
            byteIndex = bitIndex // 8
            byteIndex += D64Utility.getFontDataOffset(recordData)
            byteIndex += setWidth * row
            bitOffset= bitIndex % 8
            bitsCopied = 0

            while bitsCopied < width:
                if byteIndex >= len(recordData):
                    # Shouldn't happen, but I've seen fonts
                    # (MEGA BRUSHSTROKE) where it does.
                    byte = 0
                else:
                    byte = recordData[byteIndex]
                fontBits = min(8 - bitOffset, width - bitsCopied)
                i = bitOffset
                while i < bitOffset + fontBits:
                    mask = 1 << (7 - i)
                    rawImage.setPixel(QPoint(rasterX, row), 0 if byte & mask else 1)
                    i += 1; rasterX += 1
                bitsCopied += fontBits
                bitOffset= 0 # for bytes after the first one
                byteIndex += 1
        row += 1
    if doubleSize:
        rawImage = rawImage.scaled(QSize(textWidth * 2, height * 2))
    image = QPixmap.fromImage(rawImage)
    return image

#======================================================================

class GeoPaintPreviewer:
    def __init__(self):
        # "Pepto" colors (https://www.pepto.de/projects/colorvic/2001/):
        self.peptoColors = [
            0xFF000000, # black
            0xFFFFFFFF, # white
            0xFF68372B, # red
            0xFF70A4B2, # cyan
            0xFF6F3D86, # purple
            0xFF588D43, # green
            0xFF352879, # blue
            0xFFB8C76F, # yellow
            0xFF6F4F25, # orange
            0xFF433900, # brown
            0xFF9A6759, # light red
            0xFF444444, # dark grey
            0xFF6C6C6C, # medium grey
            0xFF9AD284, # light green
            0xFF6C5EB5, # light blue
            0xFF959595  # light grey
        ]
        self.recordBytes = [0] * ImageParams.BUFFER_SIZE.value

    def getGeoPaintPreview(self, dirEntry: DirEntry, diskImage : DiskImage):
        """
        Get a preview image of a geoPaint file.
        :param self:
        :param dirEntry: The directory entry for the file to display.
        :param diskImage: The file's disk image.
        :return: A QPixmap that can be attached to a QLabel.
        """
        self.card = 0; self.row = 0  # coordinates into image
        self.cardRow = 0  # two card rows per VLIR record

        #--------------------------------------------
        # Get height of image (width is always 640).
        #--------------------------------------------
        logging.info(f"previewing geoPaint image {dirEntry.getDisplayFileName()}")
        index = diskImage.getGeosVlirIndex(dirEntry)
        record = 0; records = 0
        # geoPaint files have 45 records (0-44) of two card rows each,
        # or fewer if the image is shorter (width is always the same)
        while record < 45:
            offset = (record + 1) * 2  # convert VLIR record no. to sector index
            if index[offset]: # non-empty record
                records += 1
            record += 1
        if records < 45:
            logging.debug(f"{records} non-empty records found, image will be {records * 16} pixels tall")
            self.rawImage = QImage(QSize(640, 16 * records), QImage.Format.Format_Indexed8)
        else:
            self.rawImage = QImage(QSize(640, 720), QImage.Format.Format_Indexed8)
            self.rawImage.fill(15) # clear it with default GEOS background color

        # set up color table
        i = 0
        while i < 16:
            self.rawImage.setColor(i, self.peptoColors[i])
            i += 1

        # -------------------------------------------------
        # Decompress data and plot pixels with color data.
        # -------------------------------------------------
        record = 0
        # while record < (45 if not foundEmpty else firstEmpty):
        while record < 45:
            try:
                self.vlirBuffer = diskImage.readVlirRecord(record, dirEntry)
            except Exception as exc:
                logging.exception(exc)
                record += 1
                continue
            self.vlirIndex = 0; dataIndex = 0
            # decompress pixel and color data:
            try:
                self.processRecord(self.recordBytes, dataIndex, ImageParams.BUFFER_SIZE.value)
            except Exception as exc:
                raise exc
            # plot pixels with color data for this record
            self.colorIndex = ImageParams.DATA_SIZE.value + 8  # start of color data
            self.dataIndex = 0
            while self.colorIndex < ImageParams.BUFFER_SIZE.value:
                # process pixel data for this color card
                self.nextCard(self.recordBytes[self.colorIndex])
                self.colorIndex += 1
            record += 1

        return QPixmap.fromImage(self.rawImage)

    def processRecord(self, outBuffer, index, limit):
        """
        Decompress a single record to the combined pixel and color buffer.
        :param outBuffer: Output buffer for decompressed data.
        :param index: Index into output buffer.
        :param limit: Size of output buffer.
        """
        byteCount = 0; firstTime = True
        while byteCount < limit:
            if self.vlirIndex >= len(self.vlirBuffer):
                logging.debug(f"Missing data: index is {self.vlirIndex}, VLIR record is {len(self.vlirBuffer)}")
                raise Exception("This geoPaint file is corrupt (missing data).")
            cmd = self.vlirBuffer[self.vlirIndex]
            self.vlirIndex += 1  # point to data
            if not cmd:
                logging.debug("COMMAND IS NULL BYTE")
                break

            if cmd < 64:  # next "count" bytes are data
                count = cmd
                cmdHex = format(cmd, "02x")
                # logging.debug(f"at vlirIndex {hex(self.vlirIndex - 1)}, cmd ${cmdHex}: next {count} bytes are data")
                if byteCount + count > limit: # as the saying goes, "this should never happen"
                    count = limit - byteCount
                    adjustment = cmd - count
                    logging.debug(f"count adjusted from {cmd} to {count} (adjustment of {adjustment})")
                byteCount += count
                j = 0
                while j < count:
                    if self.vlirIndex + j >= len(self.vlirBuffer):
                        logging.debug(f"Missing data: index is {self.vlirIndex + j}, VLIR buffer size is {len(self.vlirBuffer)}")
                        raise Exception("This geoPaint file is corrupt (missing data).")
                    outBuffer[index] = self.vlirBuffer[self.vlirIndex + j]
                    index += 1
                    j += 1
                self.vlirIndex += count  # point to next command

            elif cmd < 128:  # repeat next card (eight bytes) "count" times
                count = cmd - 64
                cmdHex = format(cmd, "02x")
                # logging.debug(f"at vlirIndex {hex(self.vlirIndex - 1)}, cmd ${cmdHex}: repeat next 8-byte card {count} times")
                if byteCount + count > limit: # as the saying goes, "this should never happen"
                    count = limit - byteCount
                    adjustment = (cmd - 64) - count
                    logging.debug(f"count adjusted from {cmd - 64} to {count} (adjustment of {adjustment})")
                byteCount += count * 8
                j = 0
                while j < count:
                    k = 0
                    while k < 8:
                        if self.vlirIndex + k >= len(self.vlirBuffer):
                            logging.debug(f"Missing data: index is {self.vlirIndex + k}, buffer size is {len(self.vlirBuffer)}")
                            raise Exception("This geoPaint file is corrupt (missing data).")
                        outBuffer[index] = self.vlirBuffer[self.vlirIndex + k]
                        index += 1
                        k += 1
                    j += 1
                self.vlirIndex += 8  # point to next command

            else:  # repeat next byte "count" times
                count = cmd - 128
                cmdHex = format(cmd, "02x")
                # logging.debug(f"at vlirIndex {hex(self.vlirIndex - 1)}, cmd ${cmdHex}: repeat next byte {count} times")
                if byteCount + count > limit: # as the saying goes, "this should never happen"
                    count = limit - byteCount
                    adjustment = (cmd - 128) - count
                    logging.debug(f"count adjusted from {cmd - 128} to {count} (adjustment of {adjustment})")
                byteCount += count
                j = 0
                while j < count:
                    if self.vlirIndex >= len(self.vlirBuffer):
                        logging.debug(f"Missing data: index is {self.vlirIndex}, buffer size is {len(self.vlirBuffer)}")
                        raise Exception("This geoPaint file is corrupt (missing data).")
                    outBuffer[index] = self.vlirBuffer[self.vlirIndex]
                    index += 1
                    j += 1
                self.vlirIndex += 1  # point to next command

    #=======================================================================
    # Plot a single card of data.
    #=======================================================================
    def nextCard(self, colors):
        """
        Plot the 64 pixels of a card (8 rows).
        :param colors: Card's color data (4 bits each foreground/background).
        :return:
        """
        fg = (colors & 0xf0) >> 4
        bg = colors & 0x0f
        i = 0
        while i < 8:  # i is line (byte) counter within card
            pixelData = self.recordBytes[self.dataIndex]
            j = 0
            while j < 8:  # j is bits within this card line
                mask = (1 << (7 - j))
                data = fg if pixelData & mask else bg
                try:
                    x = (self.card * 8) + j
                    y = self.row + i
                    if x >= 640 or y >= 720:
                        logging.debug(f"OUT OF RANGE, x: {x}, y: {y}")
                    self.rawImage.setPixel(QPoint(x, y), data)
                except Exception as exc:
                    logging.exception(exc)
                j += 1
            i += 1
            self.dataIndex += 1

        self.card += 1
        if self.card == 80:  # end of card row
            self.cardRow += 1
            self.card = 0
        self.row = self.cardRow * 8  # top row, incremented by i

