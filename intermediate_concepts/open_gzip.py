import StringIO
import urllib2
import gzip
import struct
import re

REGEX = b'google-talkplugin(?:[-_]?(?:minsrc|src|source))?[-_]([^-/_\s]+?)(?i)(?:[-_]'\
    '(?:minsrc|src|source))?\.(?:tar|t[bglx]z|tbz2|zip|rpm)'
"""
url = "https://dl.google.com/linux/talkplugin/rpm/stable/x86_64/repodata/primary.xml.gz"


request = urllib2.Request(url)
request.add_header('Accept-encoding', 'gzip')
response = urllib2.urlopen(request)
content = response.read()
response.close()
fh=StringIO.StringIO(content)
html = gzip.GzipFile(fileobj=StringIO.StringIO(content))
try:
    for line in html:
        line=line.rstrip()
except struct.error:
    pass
"""

text = '<?xml version="1.0" encoding="UTF-8"?><metadata xmlns="http://linux.duke.edu/metadata/common" xmlns:rpm="http://linux.duke.edu/metadata/rpm" packages="1"><package type="rpm"><name>google-talkplugin</name><arch>x86_64</arch><version epoch="0" ver="5.40.2.0" rel="1"/><checksum type="sha" pkgid="YES">1fde513103c24c339547ffdacd998d11a89e0a0a</checksum><summary>Google Talk Plugin</summary><description>The Google Talk Plugin is a browser plugin that enables you to use Google voice and video chat to chat face to face with family and friends. This product includes software developed by the OpenSSL Project for use in the OpenSSL Toolkit (http://www.openssl.org/). This product includes cryptographic software written by Eric Young (eay@cryptsoft.com).</description><packager>Voice and Video Chat Linux Team &lt;voice-and-video-linux-packager@google.com&gt;</packager><url>http://www.google.com/chat/video</url><time file="1422573195" build="1422470372"/><size package="7732331" installed="17284551" archive="17324720"/><location href="google-talkplugin-5.40.2.0-1.x86_64.rpm"/><format><rpm:license>Proprietary (see http://www.google.com/talk/terms.html)</rpm:license><rpm:vendor>Google, Inc.</rpm:vendor><rpm:group>Applications/Internet</rpm:group><rpm:buildhost>uml</rpm:buildhost><rpm:sourcerpm>google-talkplugin-5.40.2.0-1.src.rpm</rpm:sourcerpm><rpm:header-range start="456" end="45748"/><rpm:provides><rpm:entry name="libnpgoogletalk.so()(64bit)"/><rpm:entry name="libgoogletalkremoting.so()(64bit)"/><rpm:entry name="google-talkplugin(x86-64)" flags="EQ" epoch="0" ver="5.40.2.0" rel="1"/><rpm:entry name="libppo1d.so()(64bit)"/><rpm:entry name="libnpo1d.so()(64bit)"/><rpm:entry name="libppgoogletalk.so()(64bit)"/><rpm:entry name="google-talkplugin" flags="EQ" epoch="0" ver="5.40.2.0" rel="1"/></rpm:provides><rpm:requires><rpm:entry name="libgthread-2.0.so.0()(64bit)"/><rpm:entry name="rtld(GNU_HASH)"/><rpm:entry name="libgcc_s.so.1(GCC_3.0)(64bit)"/><rpm:entry name="libm.so.6(GLIBC_2.2.5)(64bit)"/><rpm:entry name="libXext.so.6()(64bit)"/><rpm:entry name="libXrender.so.1()(64bit)"/><rpm:entry name="libstdc++.so.6()(64bit)"/><rpm:entry name="libc.so.6(GLIBC_2.14)(64bit)"/><rpm:entry name="libgdk-x11-2.0.so.0()(64bit)"/><rpm:entry name="libgcc_s.so.1()(64bit)"/><rpm:entry name="libXfixes.so.3()(64bit)"/><rpm:entry name="libasound.so.2()(64bit)"/><rpm:entry name="libstdc++.so.6(GLIBCXX_3.4.15)(64bit)"/><rpm:entry name="libstdc++.so.6(GLIBCXX_3.4)(64bit)"/><rpm:entry name="libstdc++.so.6(CXXABI_1.3.1)(64bit)"/><rpm:entry name="libm.so.6()(64bit)"/><rpm:entry name="librt.so.1(GLIBC_2.2.5)(64bit)"/><rpm:entry name="libpthread.so.0(GLIBC_2.3.3)(64bit)"/><rpm:entry name="libX11.so.6()(64bit)"/><rpm:entry name="rpmlib(PayloadFilesHavePrefix)" flags="LE" epoch="0" ver="4.0" rel="1"/><rpm:entry name="libv4l2.so.0()(64bit)"/><rpm:entry name="libstdc++.so.6(GLIBCXX_3.4.9)(64bit)"/><rpm:entry name="/bin/sh"/><rpm:entry name="libc.so.6(GLIBC_2.3.3)(64bit)"/><rpm:entry name="libXcomposite.so.1()(64bit)"/><rpm:entry name="libpulse.so.0()(64bit)"/><rpm:entry name="libc.so.6(GLIBC_2.7)(64bit)"/><rpm:entry name="libc.so.6(GLIBC_2.3.4)(64bit)"/><rpm:entry name="libXrandr.so.2()(64bit)"/><rpm:entry name="libgdk_pixbuf-2.0.so.0()(64bit)"/><rpm:entry name="libanl.so.1()(64bit)"/><rpm:entry name="libgtk-x11-2.0.so.0()(64bit)"/><rpm:entry name="libpthread.so.0(GLIBC_2.2.5)(64bit)"/><rpm:entry name="libpthread.so.0(GLIBC_2.3.2)(64bit)"/><rpm:entry name="libc.so.6(GLIBC_2.3)(64bit)"/><rpm:entry name="libc.so.6()(64bit)"/><rpm:entry name="libstdc++.so.6(GLIBCXX_3.4.11)(64bit)"/><rpm:entry name="libgobject-2.0.so.0()(64bit)"/><rpm:entry name="rpmlib(CompressedFileNames)" flags="LE" epoch="0" ver="3.0.4" rel="1"/><rpm:entry name="libc.so.6(GLIBC_2.4)(64bit)"/><rpm:entry name="libdl.so.2()(64bit)"/><rpm:entry name="libcairo.so.2()(64bit)"/><rpm:entry name="at"/><rpm:entry name="libc.so.6(GLIBC_2.2.5)(64bit)"/><rpm:entry name="libglib-2.0.so.0()(64bit)"/><rpm:entry name="libstdc++.so.6(CXXABI_1.3)(64bit)"/><rpm:entry name="libpthread.so.0()(64bit)"/><rpm:entry name="libexpat.so.1()(64bit)"/><rpm:entry name="libdl.so.2(GLIBC_2.2.5)(64bit)"/><rpm:entry name="librt.so.1()(64bit)"/><rpm:entry name="libpango-1.0.so.0()(64bit)"/></rpm:requires><file>/etc/cron.daily/google-talkplugin</file><file type="dir">/etc/cron.daily</file></format></package> </metadata>'

print re.findall(b'google-talkplugin(?:[-_]?(?:minsrc|src|source))?[-_]([^-/_\s]+?)(?i)(?:[-_](?:minsrc|src|source))?\.(?:tar|t[bglx]z|tbz2|zip)', text)
