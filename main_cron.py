#!/usr/bin/env python3

import model, mturk, tweet_sender, time
from housepy import config, log, process

ts = tweet_sender.TweetSender()

process.secure_pid(os.path.join(os.path.dirname(__file__), "run"))

while True:
    clips = model.get_recent()
    for clip in clips:
        log.info("Checking hit_id %s" % clip['hit_id'])
        text = mturk.retrieve_result(clip['hit_id'])        
        if text is not None:
            model.mark_clip(clip['t'])
            ts.queue.put(text)
    time.sleep(10)
