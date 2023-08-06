# Snacker-Tracker/Scanner

This is the bit that just reads a barcode scanner and transmits over the wire.

Most barcode scanners I've seen basically act like a keyboard that just "types" the code as you scan items. If we were running this in the foreground, it'd be pretty simple, but since we're running this in the background as a systemd unit, then we need to capture that input from a special device type. That abstraction is done by the `evdev` lib.
