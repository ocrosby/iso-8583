# ISO 8583

## ISO 8583 Message Structure

The ISO 8583 message consists of a Message Type Indicator, Bitmaps, and Data Elements.

A **Message Type Indicator** is a 4 digit numeric field that describres each message class and function.

### Bitmap

Bit map(s) follow the message type identifier.  A single bit map consists of sixty-four (64) bits or sixteen 
hexadeciamal characters positions from left to right.  Each bit denotes the presence or absense of the corresponding 
data element.

Two bit maps can exist on an ISO 8583 message.  The first bit map is the primary bit map and is always present.  
The secondary bitmap indicates the presence of data elements 65 to 128.  Each data element represents a certain usage 
in the standard ISO 8583 message.  Most commonly used data elements are usually represented in the primary bitmap.

The first bit of the primary bitmap signifies if the secondary bitmap is present.  If the first bit is set to 1, 
then the secondary bitmap is present.  If the first bit is set to 0, then the secondary bitmap is not present.


## References
* [ISO 8583](https://en.wikipedia.org/wiki/ISO_8583)
* [ISO 8583 on GitHub](https://github.com/moov-io/iso8583/blob/master/README.md)
* [ISO 8583:1987](https://www.iso.org/standard/17742.html)
* [ISO 8583:2003](https://www.iso.org/standard/39527.html)
* [ISO 8583:2003 - Wikipedia](https://en.wikipedia.org/wiki/ISO_8583#ISO_8583:2003)
