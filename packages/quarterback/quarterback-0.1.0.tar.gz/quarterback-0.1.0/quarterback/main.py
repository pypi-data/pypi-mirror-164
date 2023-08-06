from io import BytesIO

import pandas as pd
from minio import Minio
from opcua import Client
from pendulum import datetime, instance, now
from rocketry import Rocketry
from rocketry.args import Return
from rocketry.conds import (after_all_success, after_any_fail, after_success,
                            cron)


class OpcuaMinio:
    def __init__(self) -> None:
        self.interval = 10
        self.period = 1

    def connect_opcua(self, server_opcua) -> None:
        self.client_opcua = Client(server_opcua)

    def connect_minio(self, url, access_key, secret_key, secure) -> None:
        self.client_minio = Minio(
            url,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure,
        )

    def set_interval(self, interval: int):
        self.interval = interval

    def get_values(self, nodes):

        self.client_opcua.connect()

        datetime_end = now()
        datetime_start = datetime_end.subtract(minutes=self.period)

        result = {"Timestamp": []}

        for node_id in nodes:

            node = self.client_opcua.get_node(node_id)

            display_name = node.get_browse_name().Name
            result[display_name] = []

            values = node.read_raw_history(
                datetime_start,
                datetime_end,
            )

            for value in values:

                timestamp = instance(value.ServerTimestamp)

                time_min, time_seg = timestamp.minute, timestamp.second
                time_seg += time_min * 60

                if (
                    not time_seg % self.interval
                    and value.StatusCode.name == "Good"
                ):
                    result[display_name].append(value.Value.Value)
                    if timestamp not in result["Timestamp"]:
                        result["Timestamp"].append(timestamp)

        self.client_opcua.disconnect()
        return result

    def upload_minio(self, data, bucket):

        df = pd.DataFrame.from_dict(data)
        csv_bytes = df.to_csv(index=False).encode("utf-8")
        csv_buffer = BytesIO(csv_bytes)

        file_name = df["Timestamp"][0]

        self.client_minio.put_object(
            bucket,
            f"{file_name}.csv",
            data=csv_buffer,
            length=len(csv_bytes),
            content_type="application/csv",
        )

    def run(self, nodes, bucket):
        sched = Rocketry()

        @sched.task(cron(f"*/{self.period} * * * *"), name="get_values")
        def _fetch():
            return self.get_values(nodes)

        @sched.task(after_success("get_values"), name="upload_minio")
        def _send(data=Return("get_values")):
            self.upload_minio(data, bucket)

        @sched.task(after_all_success("get_values", "upload_minio"))
        def _success():
            print(f"success at {now()}")

        @sched.task(after_any_fail("get_values", "upload_minio"))
        def _fail():
            print(f"fail at {now()}")

        sched.run()
