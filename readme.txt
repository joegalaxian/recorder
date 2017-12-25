OBJECTIVE
---------
This firectory contain scripts and files related to the radio show Gente Sexy and its records.

FILES AND DIRECTORIES
---------------------
save/       : Output directory.
dev/        : Development folder - sandbox.
ver/        : Older/archived versions.
test/       : Misc. tests.

reclite.py  : Lite recorder script (v1), main function record(stream_url).
              Records stream URL into mp3 'output.mp3' indefenitly, until exception (timeout, CTRL+C).
              Usage: python reclite.py <stream_url>

recorder.py : Recorder module (v5), main function record().
              
main.py     : Application recorder script (v5), based on record.record().
              Usage: python main.py <url> [-h] [-t <timeout>] [-o <output>] [-v]
	
                <url>        (required) : stream URL
                -h           (optional) : prints this help message
                -o <output>  (optional) : output filename, 'YYYYMMDD_hhmmss.mp3' by default
                -t <timeout> (optional) : timeout in seconds, indefinitely by default
                -v           (optional) : verbose mode

rec.py       : Improved recorder script (v6), main function 'rec(stream_url, timeout=None)'.
               Records stream URL into './save/gentesexy_YYYYMMDD_HHMISS.mp3'
               Automatically reconnects in 30s, if connection is dropped or timed out.
               Usage: python rec.py <stream_url> [<timeout>]

gentesexy    : Binary executable based on 'rec.py'.
               Records Blue FM into 'save/gentesexy_YYYYMMDD_HHMISS.mp3' with timeout set to 15000s (4h).
               Automatic reconnect in 30s if connection dropped.

gentesexy_old: Binary executable based on 'recorder.py'.
               Records Blue FM into 'save/gentesexy_YYYYMMDD_HHMISS.mp3' with timeout set to 15000s (4h).

urls.txt     : List of stream URLs.

AUTOMATION
----------
Automation is done using cron.
Check crontab job list: crontab -l

cronjob_gentesexy.sh   : sh script that executes 'gentesexy'.
cronjob_gentesexy.cron : cron file that executes 'cronjob_gentesexy.sh' every day at 23:01:00.

