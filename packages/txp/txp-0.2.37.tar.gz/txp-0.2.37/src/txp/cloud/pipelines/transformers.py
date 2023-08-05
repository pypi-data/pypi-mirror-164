import apache_beam as beam
import logging


class TimeProcessing(beam.DoFn):

    def to_runner_api_parameter(self, unused_context):
        return "beam:transforms:custom_parsing:custom_v0", None

    def process(self, element, timestamp=beam.DoFn.TimestampParam, window=beam.DoFn.WindowParam):
        import google.cloud.firestore as firestore
        from txp.cloud.common import utils as cu

        firestore_db = firestore.Client()
        mode = cu.get_signal_mode_from_firestore(element["configuration_id"], element["tenant_id"],
                                                 element["edge_logical_id"], element["perception_name"], firestore_db)
        if mode is None or not cu.SignalMode.is_time(mode):
            return

        yield element


class FftProcessing(beam.DoFn):

    def to_runner_api_parameter(self, unused_context):
        return "beam:transforms:custom_parsing:custom_v0", None

    def process(self, element, timestamp=beam.DoFn.TimestampParam, window=beam.DoFn.WindowParam):
        from scipy.fft import fft
        import google.cloud.firestore as firestore
        from txp.cloud.common import utils as cu

        firestore_db = firestore.Client()
        mode = cu.get_signal_mode_from_firestore(element["configuration_id"], element["tenant_id"],
                                                 element["edge_logical_id"], element["perception_name"], firestore_db)
        if mode is None or not cu.SignalMode.is_fft(mode):
            return
        data = [list(dimension["values"]) for dimension in element["data"]]
        fft_data = []
        for index, dimension_signal_sample in enumerate(data):
            fft_data.append({
                "values": [],
                "index": index
            })
            n = len(fft_data)
            for z in fft(dimension_signal_sample):
                fft_data[n - 1]["values"].append({"real": float(z.real), "imag": float(z.imag)})

        yield {
            "fft": fft_data,
            "package_timestamp": element["package_timestamp"],
            "perception_name": element["perception_name"],
            "edge_logical_id": element["edge_logical_id"],
            "signal_timestamp": element["signal_timestamp"],
            "configuration_id": element["configuration_id"],
            "observation_timestamp": element["observation_timestamp"],
            "gateway_task_id": element["gateway_task_id"],
            "sampling_window_index": element["sampling_window_index"],
            "number_of_sampling_windows": element["number_of_sampling_windows"],
            "tenant_id": element["tenant_id"],
            "partition_timestamp": element["partition_timestamp"]
        }


class PsdProcessing(beam.DoFn):

    def to_runner_api_parameter(self, unused_context):
        return "beam:transforms:custom_parsing:custom_v0", None

    def process(self, element, timestamp=beam.DoFn.TimestampParam, window=beam.DoFn.WindowParam):
        import google.cloud.firestore as firestore
        from txp.cloud.common import utils as cu
        from txp.cloud.common import metrics

        firestore_db = firestore.Client()
        mode = cu.get_signal_mode_from_firestore(element["configuration_id"], element["tenant_id"],
                                                 element["edge_logical_id"], element["perception_name"], firestore_db)
        if mode is None or not cu.SignalMode.is_psd(mode):
            return
        data = [list(dimension["values"]) for dimension in element["data"]]
        data_psd = []
        for index, dimension_signal_sample in enumerate(data):
            f, psd = metrics.get_psd(dimension_signal_sample, cu.get_sampling_frequency(element, firestore_db))
            data_psd.append({
                "psd": [float(e) for e in psd],
                "frequency": [float(e) for e in f],
                "index": index,
            })

        yield {
            "data": data_psd,
            "package_timestamp": element["package_timestamp"],
            "perception_name": element["perception_name"],
            "edge_logical_id": element["edge_logical_id"],
            "signal_timestamp": element["signal_timestamp"],
            "configuration_id": element["configuration_id"],
            "observation_timestamp": element["observation_timestamp"],
            "gateway_task_id": element["gateway_task_id"],
            "sampling_window_index": element["sampling_window_index"],
            "number_of_sampling_windows": element["number_of_sampling_windows"],
            "tenant_id": element["tenant_id"],
            "partition_timestamp": element["partition_timestamp"]
        }


class TimeMetrics(beam.DoFn):

    def to_runner_api_parameter(self, unused_context):
        return "beam:transforms:custom_parsing:custom_v0", None

    def process(self, element, timestamp=beam.DoFn.TimestampParam, window=beam.DoFn.WindowParam):
        from txp.cloud.common import metrics
        import google.cloud.firestore as firestore
        from txp.cloud.common import utils as cu

        firestore_db = firestore.Client()
        mode = cu.get_signal_mode_from_firestore(element["configuration_id"], element["tenant_id"],
                                                 element["edge_logical_id"], element["perception_name"], firestore_db)
        if mode is None or cu.SignalMode.is_image(mode):
            return

        for dimension in range(0, len(element["data"])):
            yield {
                "observation_timestamp": element["observation_timestamp"],
                "edge_logical_id": element["edge_logical_id"],
                "perception_name": element["perception_name"],
                "signal_timestamp": element["signal_timestamp"],
                "package_timestamp": element["package_timestamp"],
                "dimension": dimension,
                "configuration_id": element["configuration_id"],
                "peak": float(metrics.peak(element["data"][dimension]["values"])),
                "rms": float(metrics.rms(element["data"][dimension]["values"])),
                "standard_deviation": float(metrics.standard_deviation(element["data"][dimension]["values"])),
                "crest_factor": float(metrics.crest_factor(element["data"][dimension]["values"])),
                "gateway_task_id": element["gateway_task_id"],
                "sampling_window_index": element["sampling_window_index"],
                "number_of_sampling_windows": element["number_of_sampling_windows"],
                "tenant_id": element["tenant_id"],
                "partition_timestamp": element["partition_timestamp"]
            }


class FftMetrics(beam.DoFn):

    def to_runner_api_parameter(self, unused_context):
        return "beam:transforms:custom_parsing:custom_v0", None

    def process(self, element, timestamp=beam.DoFn.TimestampParam, window=beam.DoFn.WindowParam):
        from txp.cloud.common import metrics
        from txp.cloud.common import utils as cu

        data_per_dimension = cu.get_fft_as_np_array(element["fft"])
        for dimension in range(0, len(data_per_dimension)):
            data = data_per_dimension[dimension].real
            yield {
                "edge_logical_id": element["edge_logical_id"],
                "perception_name": element["perception_name"],
                "signal_timestamp": element["signal_timestamp"],
                "package_timestamp": element["package_timestamp"],
                "dimension": dimension,
                "configuration_id": element["configuration_id"],
                "peak": float(metrics.peak(data)),
                "rms": float(metrics.rms(data)),
                "standard_deviation": float(metrics.standard_deviation(data)),
                "crest_factor": float(metrics.crest_factor(data)),
                "observation_timestamp": element["observation_timestamp"],
                "gateway_task_id": element["gateway_task_id"],
                "sampling_window_index": element["sampling_window_index"],
                "number_of_sampling_windows": element["number_of_sampling_windows"],
                "tenant_id": element["tenant_id"],
                "partition_timestamp": element["partition_timestamp"]
            }


class PsdMetrics(beam.DoFn):

    def to_runner_api_parameter(self, unused_context):
        return "beam:transforms:custom_parsing:custom_v0", None

    def process(self, element, timestamp=beam.DoFn.TimestampParam, window=beam.DoFn.WindowParam):
        from txp.cloud.common import metrics
        import numpy as np

        for dimension in range(0, len(element["data"])):
            f = element["data"][dimension]["frequency"]
            psd = element["data"][dimension]["psd"]
            integrated_psd = metrics.integrate(psd, x=f)
            yield {
                "observation_timestamp": element["observation_timestamp"],
                "edge_logical_id": element["edge_logical_id"],
                "perception_name": element["perception_name"],
                "signal_timestamp": element["signal_timestamp"],
                "package_timestamp": element["package_timestamp"],
                "dimension": dimension,
                "configuration_id": element["configuration_id"],
                "rms": float(np.sqrt(integrated_psd[-1])),
                "standard_deviation": float(metrics.standard_deviation(psd)),
                "crest_factor": float(metrics.crest_factor(psd)),
                "peak_frequency": float(metrics.peak(f)),
                "peak_amplitude": float(metrics.peak(psd)),
                "gateway_task_id": element["gateway_task_id"],
                "sampling_window_index": element["sampling_window_index"],
                "number_of_sampling_windows": element["number_of_sampling_windows"],
                "tenant_id": element["tenant_id"],
                "partition_timestamp": element["partition_timestamp"]
            }


class WriteToBigQuery(beam.DoFn):

    def to_runner_api_parameter(self, unused_context):
        return "beam:transforms:custom_parsing:custom_v0", None

    def process(self, element, table_id, timestamp=beam.DoFn.TimestampParam, window=beam.DoFn.WindowParam):
        from google.cloud import bigquery
        from datetime import datetime
        import json

        keys_to_ignore = ["gateway_task_id", "sampling_window_index", "number_of_sampling_windows"]
        bigquery_element = {k: element[k] for k in element if k not in keys_to_ignore}
        client = bigquery.Client()
        table_id = table_id.replace(":", ".")
        errors = client.insert_rows_json(table_id, [bigquery_element])
        message = f"""Edge: {element["edge_logical_id"]}
        Perception: {element["perception_name"]}
        Signal Timestamp: {datetime.fromtimestamp(
            element["signal_timestamp"] // 1e9).strftime('%Y-%m-%d %H:%M:%S')}
        Package Timestamp: {datetime.fromtimestamp(
            element["package_timestamp"] // 1e9).strftime('%Y-%m-%d %H:%M:%S')}
        """
        if not errors:
            logging.info(f"""Storing in {table_id}: {message} """)

            res = {
                "table_id": table_id,
                "edge_logical_id": element["edge_logical_id"],
                "perception_name": element["perception_name"],
                "package_timestamp": element["package_timestamp"],
                "signal_timestamp": element["signal_timestamp"],
                "observation_timestamp": element["observation_timestamp"],
                "configuration_id": element["configuration_id"],
                "gateway_task_id": element["gateway_task_id"],
                "sampling_window_index": element["sampling_window_index"],
                "number_of_sampling_windows": element["number_of_sampling_windows"],
                "tenant_id": element["tenant_id"],
                "partition_timestamp": element["partition_timestamp"]
            }
            if "previous_part_index" in element:
                res["previous_part_index"] = element["previous_part_index"]
            if "part_index" in element:
                res["part_index"] = element["part_index"]
            if "dimension" in element:
                res["dimension"] = element["dimension"]

            res = json.dumps(res).encode('utf-8')

            yield res
        else:
            logging.error(f"""Could not store in {table_id}: {message}, ERROR: {errors} """)
