import binascii 

from Image import * 

class FileType:
    extention = ''

    def __init__(self, file):
        '''
        Module voor het achterhalen van de gebruikte filetypes
        :param file: FSFileInfo Object
        '''
        # Opslaan belangrijke parameters
        self.file = file
        # extentie achter . zoeken in file
        if '.' in self.file.name: 
            self.extention = self.file.name.split('.')[-1]  

    def analyse_header(self):
        '''
        Analyseerd header van bestand
        :return: Arraylist met mogelijke restulaten
        '''
        # Uitlezen eerste 20 bytes van file
        head = self.file.head(20)
        resultset = []

        Debugger('Requested header of file: ' + str(head))
        Debugger('Compairing Header to signatures')
        # Loopen door alle bekende signatures
        for signature in self.signatures:
            # omzetten signature naar python hex
            sig_head = binascii.unhexlify(signature['hex'])
            # vergelijken hex van signature en file header 
            if sig_head == head[:len(sig_head)]:
                # Wanneer resultaat is gevonden, toevoegen aan resultaat
                resultset.append(signature) 
        return resultset

    def analyse(self):
        '''
        Analyseerd header van bestand en selecteerd meest juiste bevinding
        :return: Array met extentie en informatie over bestand
        '''
        # Alle bekende headers ophalen
        signatures = self.analyse_header() 

        # Vergelijken van resultaten met extentie van file
        # Wanneer er meerdere signatures zijn met verschillende extenties
        # De juiste extentie selecteren bij dit bestand
        for signature in signatures: 
            if signature['ext'].lower() == self.extention.lower():
                Debugger('Extention: ' + str(signature['ext']))
                Debugger('Format: ' + str(signature['format'])) 
                return [signature['ext'], signature['format']]

        # Eerste signature gebruiken wanneer er maar een beschikbaar is
        if len(signatures) > 0:
            Debugger('Extention: ' + str(signatures[0]['ext']))
            Debugger('Format: ' + str(signatures[0]['format'])) 
            return [signatures[0]['ext'], signatures[0]['format']]
        
        # Wanneer er geen signature bekend is, alle data achter de . returnen
        Debugger('Did not found any matching signatures')
        return [self.extention, '']
         
        
    # Lijst met signatures van https://github.com/micahflee/johnhancock/blob/master/johnhancock.py
    # Aangevuld voor het compleet maken van de individuele opdrachten
    
    signatures = [
    {'hex':'4D5A', 'ext':'EXE', 'format':'DOS executable file'},
        # {'hex':'', 'ext':'', 'format':''},
    {'hex':'53514C6974', 'ext':'.SQLITE3', 'format':'SQLite 3'},
    {'hex':'00000100', 'ext':'ICO', 'format':'Windows icon|printer spool file'},
    {'hex':'494433', 'ext':'MP3', 'format':'MP3 audio file'},
    {'hex':'818102000200070104', 'ext':'AVB', 'format':'MS Chat Character'},
    {'hex':'81810300020007010400', 'ext':'BGB', 'format':'MS Chat Background File'},
    {'hex':'3B2068656C702E687066', 'ext':'HPF', 'format':'HP LaserJet Fonts'},
    {'hex':'4C44425800010100000000200000', 'ext':'LDB/RDB', 'format':'Internet Log File (Zone Alarm)'},
    {'hex':'5456444227', 'ext':'LOG', 'format':'Zone Alarm Data File'},
    {'hex':'9901A2043C', 'ext':'PKR', 'format':'PGP Public Key-ring File'},
    {'hex':'57696E5A6970','ext':'ZIP', 'format':'WinZip compressed archive'},
    {'hex':'504B030414000100','ext':'ZIP', 'format':'ZLock Pro encrypted ZIP'},
    {'hex':'504B537058','ext':'ZIP', 'format':'PKSFX self-extracting archive'},
    {'hex':'504B4C495445','ext':'ZIP', 'format':'PKLITE archive'},
    {'hex':'504B0506','ext':'ZIP', 'format':'PKZIP archive_2'},
    {'hex':'504B0304','ext':'ZIP', 'format':'PKZIP archive_1'},
    {'hex':'504B0708','ext':'ZIP', 'format':'PKZIP archive_3'},
    {'hex':'526172211A0700','ext':'RAR', 'format':'WinRAR compressed archive'},
    {'hex':'3C68746D6C3E0D0A3C62', 'ext':'PLG', 'format':'MS Developer Build Log'},
    {'hex':'9501CF0436', 'ext':'SKR', 'format':'PGP Secret Key-ring File'},
    {'hex':'74576263000000000000', 'ext':'SYD', 'format':'QEMM / Sysedit Backup File'},
    {'hex':'535A4444', 'ext':'??_', 'format':'MS Compress 5 File(?? Could be anything)'},
    {'hex':'4B57414A', 'ext':'??_', 'format':'MS Compress 6 File(?? Could be anything)'}, 
    {'hex':'424147', 'ext':'BAG', 'format':'BAG Archive'},
    {'hex':'425A68', 'ext':'BZ', 'format':'Bzip Archive File'},
    {'hex':'4D534346', 'ext':'CAB', 'format':'Microsoft Cabinet File'},
    {'hex':'4D4D5320', 'ext':'CKIT', 'format':'Commodore Compressed File'},
    {'hex':'303730373037', 'ext':'CPIO', 'format':'CPIO Archive File'},
    {'hex':'4352555348', 'ext':'CRU', 'format':'CRUSH Archive File'}, 
    {'hex':'91334846', 'ext':'HAP', 'format':'HAP Archive File'},
    {'hex':'28546869732066696C65', 'ext':'HQX', 'format':'Mac BinHex'},
    {'hex':'5F27A889', 'ext':'JAR', 'format':'Jar Archive File'},
    {'hex':'2D6C68352D', 'ext':'LHA', 'format':'LHA Compressed File'},
    {'hex':'4D415243', 'ext':'MARC', 'format':'MS Archive File'},
    {'hex':'4D48574B', 'ext':'MHK', 'format':'Broderbund Mohawk Archive Format'},
    {'hex':'4453', 'ext':'Q', 'format':'Quantum Archive'},
    {'hex':'526172211A07003B', 'ext':'RAR', 'format':'RAR Compressed File'},
    {'hex':'EDABEEDB', 'ext':'RPM', 'format':'Redhat Linux Archive'},
    {'hex':'53495421', 'ext':'SIT', 'format':'Stuffit v1 Archive File'},
    {'hex':'53747566664974', 'ext':'SIT', 'format':'Stuffit v5 Archive File'},
    {'hex':'484C53515A', 'ext':'SQZ', 'format':'SQZ Archive File'},
    {'hex':'417070204E616D6509', 'ext':'STF', 'format':'ShrinkToFit Compressed Archive'},
    {'hex':'554641', 'ext':'UFA', 'format':'UFA Archive File'},
    {'hex':'7863722046696C65', 'ext':'XCR', 'format':'XCR Archive File'},
    {'hex':'504B0304140000000800', 'ext':'ZIP', 'format':'Winzip 8.1'},
    {'hex':'504B3030504B0304', 'ext':'ZIP', 'format':'WINZIP Compressed'},
    {'hex':'5A4F4F20', 'ext':'ZOO', 'format':'ZOO Compressed File'},
    {'hex':'2E736E64', 'ext':'AU', 'format':'SoundMachine Audio File'},
    {'hex':'49424B1A', 'ext':'IBK', 'format':'Soundblaster Instrument Bank'},
    {'hex':'4D503344415441', 'ext':'M3D', 'format':'MPEG Audio Datafile'},
    {'hex':'4D546864', 'ext':'MIDI/MID', 'format':'Musical Instrument Digital Interface (MIDI) File'},
    {'hex':'2E7261FD', 'ext':'RA/RAM', 'format':'Real Audio File'},
    {'hex':'2E524D46', 'ext':'RM', 'format':'Real Media File'},
    {'hex':'5354455645024880', 'ext':'SND', 'format':'AU Format Sound'},
    {'hex':'437265617469766520566F6963652046696C651A', 'ext':'VOC', 'format':'Creative Sound File'},
    {'hex':'52494646', 'ext':'WAV', 'format':'Wave Audio File'},
    {'hex':'3B0D0A3B', 'ext':'ASM', 'format':'Uncompiled Assembly Code'},
    {'hex':'0000000C000000', 'ext':'ATN', 'format':'Adobe Photoshop Script'},
    {'hex':'406563686F206F66660D', 'ext':'BTM', 'format':'NDOS Batch to Memory'},
    {'hex':'23212F62696E2F73680A', 'ext':'CGI', 'format':'Common Gateway Interface Script'},
    {'hex':'2F2A202A202A202A202A', 'ext':'H', 'format':'C++ Header File'},
    {'hex':'484FF3C976332E39392E', 'ext':'OBS', 'format':'ObjectScript'},
    {'hex':'56435043483000000000', 'ext':'PCH', 'format':'MS C++ Precompiled Header File'},
    {'hex':'00000100000001480000', 'ext':'RSC', 'format':'Compiled Resources'},
    {'hex':'DCFE', 'ext':'EFX', 'format':'eFax file format'},
    {'hex':'0363080A', 'ext':'DBF', 'format':'Database File'},
    {'hex':'000100005374616E6461', 'ext':'MDB', 'format':'Microsoft Access file'},
    {'hex':'4D4C42', 'ext':'MLB', 'format':'MyLittleBase Database File'},
    {'hex':'00000041424300000000', 'ext':'ABC', 'format':'Micrografx ABC Flowcharter'},
    {'hex':'5157205665722E20', 'ext':'ABD', 'format':'Quicken Data File'},
    {'hex':'30000004150505', 'ext':'ADX', 'format':'Lotus Approach ADX File'},
    {'hex':'252150532D41646F6265', 'ext':'AI', 'format':'Adobe Illustrator'},
    {'hex':'5B7665725D', 'ext':'AMI', 'format':'Lotus Ami Pro'},
    {'hex':'5008', 'ext':'APP', 'format':'Clarion File Format'},
    {'hex':'49545346030000006000', 'ext':'CHM', 'format':'Compiled HTML Help File'},
    {'hex':'464158434F5645', 'ext':'CPE', 'format':'MS Office Fax Cover'},
    {'hex':'D0CF11E0A1B11AE1', 'ext':'DOC', 'format':'Word 10 Office 2000 File'},
    {'hex':'D0CF11E0A1B11AE1', 'ext':'DOC', 'format':'Word 8.0 Office 97 File'},
    {'hex':'D0CF11E0A1B11AE1', 'ext':'DOC', 'format':'Generic MS Office File'},
    {'hex':'504B0304140000000000', 'ext':'DOC', 'format':'Star Writer 6.0'},
    {'hex':'31BE000000AB0000', 'ext':'DOC', 'format':'MS Word for DOS v6 File'},
    {'hex':'1234567890FF', 'ext':'DOC', 'format':'MS Word 6.0 File'},
    {'hex':'7FFE340A', 'ext':'DOC', 'format':'MS Word File'},
    {'hex':'4D47582069747064', 'ext':'DS4', 'format':'Micrografix Designer 4'},
    {'hex':'4D5600FF0C0010000000', 'ext':'DST', 'format':'Micrografx Designer Template'},
    {'hex':'3C21454E54495459', 'ext':'DTD', 'format':'Xml DTD'},
    {'hex':'C5D0D3C6', 'ext':'EPS', 'format':'Adobe Encapsulated PostScript File'},
    {'hex':'00001A0007800100', 'ext':'FM3', 'format':'Lotus 123 v3 FMT File'},
    {'hex':'2000680020', 'ext':'FMT', 'format':'Lotus 123 v4 FMT File'},
    {'hex':'3C68746D6C3E', 'ext':'HTM', 'format':'HyperText Markup Language 1 File'},
    {'hex':'3C48544D4C3E', 'ext':'HTM', 'format':'HyperText Markup Language 2 File'},
    {'hex':'3C21444F4354', 'ext':'HTM', 'format':'HyperText Markup Language 3 File'},
    {'hex':'000100004D534953414D204461746162617365', 'ext':'MNY', 'format':'Microsoft Money File'},
    {'hex':'1A0000030000', 'ext':'NSF', 'format':'Lotus Notes Data File'},
    {'hex':'1A000003000011000100', 'ext':'NTF', 'format':'Lotus Notes Data File'},
    {'hex':'25504446', 'ext':'PDF', 'format':'PDF-1.2'},
    {'hex':'AC9EBD8F', 'ext':'QDF', 'format':'Quicken Data File'},
    {'hex':'5157205665722E20', 'ext':'QSD', 'format':'Quicken Data File'},
    {'hex':'7B5C727466', 'ext':'RTF', 'format':'Rich Text Format'}, 
    {'hex':'C354565362BD8AFF0000', 'ext':'TV4', 'format':'WordPerfect Insert Overflow - Doc 4'},
    {'hex':'2000604060', 'ext':'WK1', 'format':'Lotus 123 v1 Worksheet'},
    {'hex':'00001A0000100400', 'ext':'WK3', 'format':'Lotus 123 v3 Worksheet'},
    {'hex':'00001A0002100400', 'ext':'WK4', 'format':'Lotus 123 v5'},
    {'hex':'00001A001004', 'ext':'WKS', 'format':'Lotus MS Worksheet'},
    {'hex':'2000604060', 'ext':'WKS', 'format':'Lotus 123 v1 Worksheet'},
    {'hex':'FF575043', 'ext':'WP', 'format':'WordPerfect v5 or v6'},
    {'hex':'090808000005000433', 'ext':'XLB', 'format':'Microsoft Excel Workbook'},
    {'hex':'0904060000004000', 'ext':'XLM', 'format':'Microsoft Excel Macro'},
    {'hex':'0902060000001000B9045C00', 'ext':'XLS', 'format':'MS Excel v2'},
    {'hex':'D0CF11E0A1B11AE1', 'ext':'XLS', 'format':'Excel 8.0 Office 97 Type 2 File'},
    {'hex':'D0CF11E0A1B11AE1', 'ext':'XLS', 'format':'Excel 8.0 Office 97 Type 1 File'},
    {'hex':'0904060000001000F6055C00', 'ext':'XLS', 'format':'MS Excel v4 File'},
    {'hex':'FFFE3C0052004F004F00540053005400550042', 'ext':'XML', 'format':'MS Excel Document'},
    {'hex':'3C3F786D6C', 'ext':'XML', 'format':'MS Excel XML Document'}, 
    {'hex':'33444D46', 'ext':'3DMF', 'format':'3D Meta File'},
    {'hex':'2A2A544939322A2A0100586E5669', 'ext':'92I', 'format':'TI Bitmap'},
    {'hex':'414D4646', 'ext':'AMFF', 'format':'AMFF Image File'},
    {'hex':'4A47040E000000', 'ext':'ART', 'format':'AOL ART 1'},
    {'hex':'4A47030E000000', 'ext':'ART', 'format':'AOL ART 2'}, 
    {'hex':'BB010001C800C80001', 'ext':'BRK/301', 'format':'Brooktrout Fax'},
    {'hex':'737263646F6369643A', 'ext':'CAL/CALS', 'format':'CALS Raster Image'},
    {'hex':'07204D4D', 'ext':'CAM', 'format':'QV-10 Camera File'},
    {'hex':'20770002', 'ext':'CBD', 'format':'Vector Map Data Format'},
    {'hex':'45594553', 'ext':'CE1/CE2', 'format':'Computer Eyes File'},
    {'hex':'802A5FD700000800000004000000', 'ext':'CIN', 'format':'Kodac Cineon'},
    {'hex':'43616C6967617269', 'ext':'COB/SCN', 'format':'Caligari Truespace 2 File'},
    {'hex':'43505446494C45', 'ext':'CPT', 'format':'Corel Photopaint'},
    {'hex':'43414C414D5553435647', 'ext':'CVG', 'format':'Calamus'},
    {'hex':'3ADE68B1', 'ext':'DCX', 'format':'DCX Graphic File'},
    {'hex':'56697374612044454D2046696C65', 'ext':'DEM', 'format':'Vista Landscape Format'},
    {'hex':'424D36', 'ext':'DIB', 'format':'DIB Image File'},
    {'hex':'53445058', 'ext':'DPX', 'format':'Cineon Image File'},
    {'hex':'01FF02040302', 'ext':'DRW', 'format':'Micrographx Graphic'},
    {'hex':'41433130', 'ext':'DWG', 'format':'Autocad R13/R14 File'},
    {'hex':'65020102', 'ext':'ECW', 'format':'Enhanced Compressed Wavelet'},
    {'hex':'0100000058000000', 'ext':'EMF', 'format':'Enhanced Metafile Graphic'}, 
    {'hex':'53494D504C4520203D', 'ext':'FTS', 'format':'Flexible Image Transport System'},
    {'hex':'47494638', 'ext':'GIF', 'format':'ALL Types'},
    {'hex':'4850485034382D451E2B', 'ext':'GRO', 'format':'HP-48/49 GROB'},
    {'hex':'6E636F6C73', 'ext':'HDR', 'format':'ArcoInfo Binary Image'},
    {'hex':'354B5035315D2A67727280838563', 'ext':'HRU', 'format':'HRU Image'},
    {'hex':'EB3C902A', 'ext':'IMG', 'format':'GEM Raster file'},
    {'hex':'656C6D6F', 'ext':'INFI', 'format':'-D 	Infini-D Graphics File'},
    {'hex':'49574301', 'ext':'IWC', 'format':'WaveL Image'},
    {'hex':'803E445343494D', 'ext':'J6I', 'format':'Ricoh Camera Image File'},
    {'hex':'4A4946393961', 'ext':'JIF', 'format':'Jeff\'s Image Format'},
    {'hex':'0000000C6A5020200D0A870A', 'ext':'JP2', 'format':'JPEG-2000 JP2 Image'},
    {'hex':'FFD8FFE1', 'ext':'JPG', 'format':'Generic 1 JPG'},
    {'hex':'FFD8FFE0', 'ext':'JPG', 'format':'Generic 2 JPG'},
    {'hex':'FFD8FFE14ED84578696600004949', 'ext':'JPG', 'format':'Kodak'},
    {'hex':'4D4D002A', 'ext':'KDC', 'format':'Kodak Camera DC20/40/50'},
    {'hex':'36344C414E204944424C4F434B', 'ext':'L64', 'format':'64LAN Image File'},
    {'hex':'464F524D', 'ext':'LBM', 'format':'Interchange File'},
    {'hex':'49492A00080000000E0000010400', 'ext':'LDF', 'format':'LuraDocument Format'},
    {'hex':'575602004745000E', 'ext':'LWF', 'format':'LuraWave Format'},
    {'hex':'3700001042000010000000003964', 'ext':'MBM', 'format':'Psion Series 5 Bitmap'},
    {'hex':'4D474C', 'ext':'MGL', 'format':'MosASCII Graphics Library File'},
    {'hex':'7B0A202043726561746564', 'ext':'MIF', 'format':'Image Magick File'},
    {'hex':'8A4D4E470D0A1A0A', 'ext':'MNG', 'format':'Multiple Image Format'},
    {'hex':'4D5046', 'ext':'MPW/MPF', 'format':'MosASCII Project Workspace File'},
    {'hex':'44616E4D', 'ext':'MSP', 'format':'Windows Paint File'},
    {'hex':'433634', 'ext':'N64', 'format':'64NET Image File'},
    {'hex':'6E6E0A005E00', 'ext':'NCR', 'format':'NCR G4'},
    {'hex':'6E6666', 'ext':'NFF', 'format':'WorldToolKit Neutral File Format'},
    {'hex':'4E4747000100', 'ext':'NGG', 'format':'Nokia Group Graphics'},
    {'hex':'4E4C4D20010200', 'ext':'NLM', 'format':'Nokia Logo File'},
    {'hex':'4E4F4C00010006010300', 'ext':'NOL', 'format':'Nokia Operator Logo'}, 
    {'hex':'0000002000000001', 'ext':'PAT', 'format':'Gimp Pattern'},
    {'hex':'504158', 'ext':'PAX', 'format':'Secure Image File'},
    {'hex':'50340A', 'ext':'PBM', 'format':'Portable Bitmap'},
    {'hex':'6352010138093D00', 'ext':'PCD', 'format':'Kodak PhotoCD'},
    {'hex':'1B451B266C304F1B266C30451B26', 'ext':'PCL', 'format':'Page Control Language'},
    {'hex':'0A050108', 'ext':'PCX', 'format':'PC Paintbrush'}, 
    {'hex':'50350A', 'ext':'PGM', 'format':'Portable Greyscale'},
    {'hex':'5380F6344020', 'ext':'PIC', 'format':'Softimage'},
    {'hex':'504943DC30300100', 'ext':'PIC', 'format':'Psion Series 3 Bitmap'}, 
    {'hex':'50495820', 'ext':'PIX', 'format':'PABX Background'},
    {'hex':'89504E470D0A1A0A', 'ext':'PNG', 'format':'Portable Network Graphic'},
    {'hex':'889A0D12', 'ext':'PNG', 'format':'Portable Network Graphics File'},
    {'hex':'504F4C20466F726D6174', 'ext':'POL', 'format':'Polygon Model File'}, 
    {'hex':'38425053000100000000', 'ext':'PSD', 'format':'Adobe PhotoShop'},
    {'hex':'7E424B00', 'ext':'PSP', 'format':'Paint Shop Pro File'},
    {'hex':'5061696E742053686F702050726F20496D6167652046696C65', 'ext':'PSP', 'format':'Paint Shop Pro File'},
    {'hex':'514C4949464158', 'ext':'QFX', 'format':'Fax Image File'},
    {'hex':'6D6F6F76', 'ext':'QTM', 'format':'Apple Quick Time File'},
    {'hex':'464F524D41543D', 'ext':'RAD', 'format':'Radiance'},
    {'hex':'59A66A95', 'ext':'RAS', 'format':'SUN Raster File'},
    {'hex':'01DA01010003', 'ext':'RGB', 'format':'Silicon Graphics RGB'},
    {'hex':'52495833', 'ext':'RIX', 'format':'ColoRIX File'},
    {'hex':'23202449643A20', 'ext':'SID', 'format':'Seamless Image Graphic File'},
    {'hex':'4175746F43414420536C696465', 'ext':'SLB/SLD', 'format':'Slide Library File'},
    {'hex':'53746F726D3344', 'ext':'SOD', 'format':'Storm 3D Object Definition'},
    {'hex':'49492A00', 'ext':'TIF/TIFF', 'format':'TIFF Image File'},
    {'hex':'4D4D2A', 'ext':'TIF/TIFF', 'format':'TIF Image File (Motorola)'},
    {'hex':'FADEBABE0101', 'ext':'WIC', 'format':'J Wavelet Image Codec'},
    {'hex':'D323000003000000', 'ext':'WLM', 'format':'CompW Image'},
    {'hex':'D7CDC69A', 'ext':'WMF', 'format':'Windows graphics metafile'},
    {'hex':'FF57504310', 'ext':'WPG', 'format':'WordPerfect Graphic'},
    {'hex':'2356524D4C2056322E30', 'ext':'WRL', 'format':'VRML Version 2 Image'},
    {'hex':'23646566696E65', 'ext':'XBM', 'format':'XBM - X11 Bitmap'},
    {'hex':'2F2A2058504D202A2F', 'ext':'XPM', 'format':'XPM - X11 Pixmap'},
    {'hex':'436C69656E742055726C43616368', 'ext':'DAT', 'format':'IE History DAT File'},
    {'hex':'55524C20020000', 'ext':'DAT', 'format':'98 IE Cache Index dat ver 1 File'},
    {'hex':'55524C20030000', 'ext':'DAT', 'format':'98 IE Cache Index dat ver 2 File'},
    {'hex':'55524C20020000', 'ext':'DAT', 'format':'98 IE History Subfolder Index dat ver 1 File'},
    {'hex':'55524C20030000', 'ext':'DAT', 'format':'98 IE History Subfolder Index dat ver 2 File'},
    {'hex':'55524C20020000', 'ext':'DAT', 'format':'98 & XP IE History Root Index dat ver 1 File'},
    {'hex':'55524C20030000', 'ext':'DAT', 'format':'98 & XP IE History Root Index dat ver 2 File'},
    {'hex':'55524C20020000', 'ext':'DAT', 'format':'XP IE Hist Subfolder Index dat ver 1 File'},
    {'hex':'55524C20020000', 'ext':'DAT', 'format':'XP IE Hist Subfolder Index dat ver 2 File'},
    {'hex':'55524C20020000', 'ext':'DAT', 'format':'XP IE Cache Index dat ver 1 File'},
    {'hex':'55524C20030000', 'ext':'DAT', 'format':'XP IE Cache Index dat ver 1 File'},
    {'hex':'5B50686F6E655D', 'ext':'DUN', 'format':'Dial-Up Network Export File'},
    {'hex':'CFAD12FEC5FD', 'ext':'DBX', 'format':'Outlook Express Email Storage File'},
    {'hex':'3C21646F63747970652068746D6C207075626C6963', 'ext':'DCI', 'format':'AOL Web Email'},
    {'hex':'52657475726E2D506174683A203C', 'ext':'EML', 'format':'Outlook Express Email Message'},
    {'hex':'46726F6D202D20', 'ext':'EML', 'format':'Netscape Email Message'},
    {'hex':'46726F6D203F3F3F403F3F3F20', 'ext':'EML', 'format':'Eudora Email Message'},
    {'hex':'46726F6D3A20', 'ext':'EML', 'format':'Generic Email Message'},
    {'hex':'2142444E', 'ext':'PST', 'format':'Outlook 97 File'},
    {'hex':'0006156100000002000004D20000', 'ext':'HST', 'format':'Netscape HST'},
    {'hex':'574542', 'ext':'IGY', 'format':'Web Query'},
    {'hex':'5745420D0A310D0A687474703A2F', 'ext':'IQY', 'format':'Microsoft Web Query'},
    {'hex':'5F434153455F', 'ext':'CAS/CBK', 'format':'EnCase Case (or Backup) File'},
    {'hex':'FEEF01', 'ext':'GHO', 'format':'Norton Ghost Image File'},
    {'hex':'43363453207461706520696D6167652066696C65', 'ext':'T64', 'format':'C64 Tape Image'},
    {'hex':'43363420434152545249444745', 'ext':'CRT', 'format':'C64 Emul Cartridge File'},
    {'hex':'BABEEBEA', 'ext':'ANI', 'format':'NEOchrome Animation File'},
    {'hex':'4C504620', 'ext':'ANM', 'format':'DeluxePaint Animation'},
    {'hex':'3026B2758E66CF11A6D900AA0062', 'ext':'ASF', 'format':'Windows Media (ASF Compression)'},
    {'hex':'41564920', 'ext':'AVI', 'format':'Audio Video Interleave (AVI) File'},
    {'hex':'52494646', 'ext':'AVI', 'format':'AVI Type 1 File'},
    {'hex':'56445649', 'ext':'AVS', 'format':'Intel Digital Video Interface File'},
    {'hex':'44564D', 'ext':'DVM', 'format':'DVM Movie File'},
    {'hex':'52414E44', 'ext':'Filmstrip', 'format':'Adobe Filmstrip File Format'}, 
    {'hex':'494D4443', 'ext':'IC1/IC2/IC3', 'format':'Atari Image Film'},
    {'hex':'4C5A414E494D', 'ext':'LZA', 'format':'Lempel-Ziv-Oberhumer Compressed Animation'},
    {'hex':'07010100436F70797269', 'ext':'MMM', 'format':'Microsoft Media Clip'},
    {'hex':'000007B56D6F6F76', 'ext':'MOV', 'format':'QuickTime Movie File'},
    {'hex':'6D646174', 'ext':'M', 'format':';QT 	Quick Time Movie File'},
    {'hex':'000001B3', 'ext':'MPEG', 'format':'MPEG Video File'},
    {'hex':'5E405C6E534D4A504547', 'ext':'SMJPEG', 'format':'Simple Animation File'},
    {'hex':'52494646', 'ext':'ANI', 'format':'Cursor File'},
    {'hex':'4D5A9000030000000400', 'ext':'API', 'format':'Printer Info File'},
    {'hex':'B5A2B0B3B3B0A2B5', 'ext':'CAL', 'format':'Windows 3.1 Calendar'},
    {'hex':'52545353', 'ext':'CAP', 'format':'Windows NT Netmon Capture File'},
    {'hex':'4D53434600000000', 'ext':'CDM', 'format':'Windows Update File'},
    {'hex':'50C30100080028', 'ext':'CLP', 'format':'Windows Clipboard File'},
    {'hex':'43524547', 'ext':'DAT', 'format':'Windows 95 Registry Files'},
    {'hex':'5348434333', 'ext':'DAT', 'format':'Windows 3.1 Registry File (REG.DAT)'},
    {'hex':'202020202020696E7465', 'ext':'FON', 'format':'Font File'},
    {'hex':'3F5F0300', 'ext':'GID', 'format':'General Index'},
    {'hex':'504D4343', 'ext':'GRP', 'format':'MS Windows Group'},
    {'hex':'3F5F0300', 'ext':'HLP', 'format':'Windows Help File'},
    {'hex':'4C4E0200', 'ext':'HLP', 'format':'Windows Help File'},
    {'hex':'48797065725465726D69', 'ext':'HT', 'format':'HyperTerminal File'},
    {'hex':'5B4578745368656C6C466F6C6465', 'ext':'INI', 'format':'Desktop.ini Folder Setting File'},
    {'hex':'47040100', 'ext':'JOB', 'format':'Scheduled Tasks File'},
    {'hex':'7B0D0A6F206331', 'ext':'LGC', 'format':'Application Log File'},
    {'hex':'4C00000001140200', 'ext':'LNK', 'format':'Windows Shortcut File'},
    {'hex':'4C5441520001', 'ext':'LTR', 'format':'Letter File'},
    {'hex':'2A5050442D41646F6265', 'ext':'PPD', 'format':'Postscript Printer Description File'},
    {'hex':'E3828596010000', 'ext':'PWL', 'format':'Windows Password File'},
    {'hex':'5245474544495434', 'ext':'REG', 'format':'Windows NT Registry File'},
    {'hex':'0D0A5B536865', 'ext':'SCF', 'format':'Shell Command File'},
    {'hex':'3B0D0A3B205468697320697320', 'ext':'SCP', 'format':'Dial-Up Network Script'},
    {'hex':'4D5A90000300000004000000FFFF', 'ext':'SCR', 'format':'Screen Saver'},
    {'hex':'6749000078', 'ext':'SHD', 'format':'Printer Spool File'},
    {'hex':'4B490000', 'ext':'SHD', 'format':'Printer Spool File'},
    {'hex':'5245474544495434', 'ext':'SUD', 'format':'Registry Undo Files'},
    {'hex':'FF4B455942202020', 'ext':'SYS', 'format':'Keyboard driver file'}
]
