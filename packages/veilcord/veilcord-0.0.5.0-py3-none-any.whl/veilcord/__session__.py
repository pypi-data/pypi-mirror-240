from websocket import WebSocket
from json      import dumps, loads
from terminut  import printf as print
from asyncio   import sleep, create_task
from re        import search


class SessionManager:
    def __init__(
        self, 
        user_agent, 
        build_num, 
        device_type, 
        capabilities_num,
        cst_presence: dict = None
    ):
        self.session_id = None
        self.session_task = None
        self.session_on = False
        self.ws = WebSocket()
        
        self.user_agent = user_agent
        self.build_num = build_num
        self.device_type = device_type
        self.capabilities_num = capabilities_num
        self.custom_presence = cst_presence
        browser_patterns = {
            "Discord Client": r"discord/([\d.]+)",
            "Chrome": r"Chrome/([\d.]+)",
            "Firefox": r"Firefox/([\d.]+)",
            "Edge": r"Edge/([\d.]+)",
            "Safari": r"Safari/([\d.]+)",
            "Opera": r"OPR/([\d.]+)|Opera/([\d.]+)"
        }
        
        for browser, pattern in browser_patterns.items():
            match = search(pattern, user_agent)
            if match:
                self.browser = browser
                self.bversion = match.group(1)
        

    async def _wsconn(self, token):
        self.ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
        message = {
            "op": 2,
            "d": {
                "token": token,
                "capabilities": self.capabilities_num,
                "properties": {
                    "os": "Windows",
                    "browser_user_agent": self.user_agent,
                    "device": "",
                    "system_locale": "en-US",
                    "release_channel": "stable",
                    "client_build_number": self.build_num,
                    "client_event_source": None
                },
                "presence": {
                    "status": "online",
                    "since": 0,
                    "activities": [{
                        "name": "Custom Status",
                        "type": 4,
                        "state": "made by @imvast",
                        "emoji": ""
                    }],
                    "afk": False
                } if not self.custom_presence else self.custom_presence,
                "compress": False,
                "client_state": {
                    "guild_versions": {},
                    "highest_last_message_id": "0",
                    "read_state_version": 0,
                    "user_guild_settings_version": -1,
                    "user_settings_version": 2,
                    "private_channels_version": "0",
                    "api_code_version": 0
                }
            }
        }

        if self.device_type == "browser":
            message["d"]["properties"]["browser"] = str(self.browser)
            message["d"]["properties"]["browser_version"] = str(self.bversion)
            message["d"]["properties"]["os_version"] = "10"
            message["d"]["properties"]["referrer"] = "",
            message["d"]["properties"]["referring_domain"] = "",
            message["d"]["properties"]["referrer_current"] = "",
            message["d"]["properties"]["referring_domain_current"] = "",
        elif self.device_type == "app":
            message["d"]["properties"]["browser"] = "Discord Client"
            message["d"]["properties"]["browser_version"] = "22.3.2"
            message["d"]["properties"]["client_version"] = "1.0.9015"
            message["d"]["properties"]["os_version"] = "10.0.22621"
            message["d"]["properties"]["os_arch"] = "x64"
            message["d"]["properties"]["native_build_number"] = 32266
        # elif self.device_type == "mobile":
# {
#   "op": 2,
#   "d": {
#     "token": ,
#     "capabilities": 16383,
#     "properties": {
#       "os": "iOS",
#       "browser": "Discord iOS",
#       "device": "iPhone14,5",
#       "system_locale": "en-US",
#       "client_version": "202.0",
#       "release_channel": "stable",
#       "device_vendor_id": ,
#       "browser_user_agent": "",
#       "browser_version": "",
#       "os_version": "17.0",
#       "client_build_number": 51852,
#       "client_event_source": null,
#       "design_id": 0
#     },
#     "presence": {
#       "status": "unknown",
#       "since": 0,
#       "activities": [],
#       "afk": false
#     },
#     "compress": false,
#     "client_state": {
#       "guild_versions": {},
#       "highest_last_message_id": "0",
#       "read_state_version": 0,
#       "user_guild_settings_version": -1,
#       "user_settings_version": -1,
#       "private_channels_version": "0",
#       "api_code_version": 0
#     }
#   }
# }
        
        else: raise ValueError("An invalid type for getSession() was provided. Acceptable values: ['browser', 'app']")

        self.ws.send(
            dumps(message)
        )
        self.ws.send(
            dumps({ 
                "op": 4, 
                "d": { 
                    "guild_id": None, "channel_id": None, 
                    "self_mute": False, "self_deaf": False, "self_video": False,
                    "flags": 2,
                },
            })
        )
        for _ in range(5):
            try:
                result = loads(self.ws.recv())
            except Exception as e:
                # print(f"(!) Error Getting WS (probably invalid token) ({e})")
                continue
            if "heartbeat_interval" in dumps(result):
                self.rpBeat = result["d"].get("heartbeat_interval")
            if "session_id" in dumps(result):
                session_id = result['d'].get("session_id")
                self.session_id = session_id
                break
        return self.session_id

    async def keepSessionAlive(self, showHB):
        while self.session_on:
            try:
                self.ws.send(dumps({"op": 1, "d": 10}))
                if showHB: print(f"(*) Sent HB. | Next: {self.rpBeat/1000}s")
                await sleep(self.rpBeat / 1000)
            except Exception as e:
                print(f"(!) Error sending HB: {e}")
                break

    async def get_session(self, token: str, keep_alive: bool = False, show_hb: bool = False):
        try:
            session_id = await self._wsconn(token)
            if keep_alive:
                # print("[WARN] KeepAlive is experimental.", showTimestamp=False)
                self.session_on = True
                self.session_task = create_task(self.keepSessionAlive(show_hb))
                return session_id
            else:
                return session_id
        except KeyboardInterrupt:
            if self.session_on:
                self.session_on = False  # Stop the keep-alive loop
                await self.session_task  # Wait for the task to complete
            return

    def close_session(self):
        self.session_on = False
        if self.session_task is None:
            return print("(!) Cannot close an unopened session.")
        self.session_task.cancel()
        