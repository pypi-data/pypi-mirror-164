from dataclasses import dataclass, asdict
from enum import Enum
from typing import List

from torch_sdk.models.job import CreateJob
from torch_sdk.models.span import Span
from torch_sdk.models.span_context import SpanContext


@dataclass
class PipelineMetadata:
    """
    Description:
        Pipeline metadata.

    :param owner : (String) owner of the pipeline
    :param team: (String) team of the owner
    :param codeLocation: (String) location of the code
    """
    owner: str = None
    team: str = None
    codeLocation: str = None


class CreatePipeline:
    # createdAt = None
    # enabled = None
    # id = None
    # interrupt = None
    # notificationChannels = None
    # schedule = None
    # scheduled = None
    # schedulerType = None
    # updatedAt = None

    def __init__(self, uid: str, name: str,
                 description: str = None, meta: PipelineMetadata = None, **context):
        """
        Description:
            Class used for create pipeline in torch catalog
        :param uid: uid of the pipeline
        :param name: name of the pipeline
        :param description: (Optional)description of the pipeline
        :param meta: (PipelineMetadata) meta data of the pipeline
        :param context: context map of the pipeline
        """
        self.uid = uid
        self.name = name
        self.description = description
        self.context = context
        if meta is not None:
            self.meta = PipelineMetadata(owner=meta.owner, team=meta.team, codeLocation=meta.codeLocation)
        else:
            self.meta = None

    def __eq__(self, other):
        return self.uid == other.uid

    def __repr__(self):
        return f"Pipeline({self.uid!r})"

    def add_context(self, key: str, value: str):
        """
        Used to add context in context map
        :param key: key of the context
        :param value: value of the context
        :return: context dir
        """
        self.context[key] = value
        return self.context


class PipelineRunStatus(Enum):
    """
        pipeline run status
    """
    STARTED = 1
    COMPLETED = 2
    FAILED = 3
    ABORTED = 4


class PipelineRunResult(Enum):
    """
        Pipeline run result
    """
    UNKNOWN = 'UNKNOWN'
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'


class PipelineRun:

    def __init__(self, pipelineId, versionId=None, status=PipelineRunStatus.STARTED, id=None, startedAt=None,
                 finishedAt=None, result=PipelineRunResult.UNKNOWN, client=None, args=None,
                 continuationId=None, **kwrgs):
        """
        Description:
                Pipeline run used for instantiate run of the pipeline. To create new pipeline run you need to pass pipelineId, version.
        :param pipelineId: pipleline id
        :param versionId:  pipeline run current version
        :param status: status of the pipeline run
        :param id: pipeline run id
        :param startedAt: starting time
        :param finishedAt: finish time
        :param args: additional args for pipeline run
        :param result: pipeline run result
        """
        self.pipelineId = pipelineId
        self.versionId = versionId
        self.status = status
        self.args = args
        self.result = result
        self.continuationId = continuationId
        if id is not None:
            self.id = id
            self.startedAt = startedAt
            self.finishedAt = finishedAt
            self.client = client

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f"PipelineRun({self.__dict__})"

    # convert pipeline run to dict type
    def _convert_pipeline_run_to_dict(self, pipeline_run=None):
        """
            Description:
                Convert PipelineRun class instance to dict type
            :param pipeline_run: PipelineRun class instance
            :return: dict form of PipelineRun class instance
        """
        payload = pipeline_run.__dict__
        payload['status'] = pipeline_run.status.name
        payload['result'] = pipeline_run.result.name
        pipeline_run_payload = {'run': payload}
        return pipeline_run_payload

    # update run for a pipeline
    def update_pipeline_run(self, result: PipelineRunResult,
                            status: PipelineRunStatus = PipelineRunStatus.STARTED,
                            context_data: {} = None):
        """
        Description:
            used to update an existing pipeline run
        :return: updated pipelineRun class instance
        """
        update_pipeline_run = PipelineRun(
            pipelineId=self.pipelineId,
            versionId=self.versionId,
            result=result,
            args=context_data,
            status=status
        )
        payload = self._convert_pipeline_run_to_dict(update_pipeline_run)
        res = self.client.update_pipeline_run(self.id, payload)
        return res

    # convert span to dict
    def _convert_span_to_dict(self, span: Span, associatedJobUids):
        """
            Description:
                Convert Span class instance to dict type
            :param span: Span class instance
            :return: dict form of Span class instance
        """
        payload = span.__dict__
        payload['status'] = span.status.name
        span_payload = {'span': payload, 'associatedJobUids' : associatedJobUids }
        return span_payload

    # create span for pipeline run
    def create_span(self, uid: str, context_data: dict = None, associatedJobUids = None ):
        """
        Description:
            used to create span for any pipeline run
        :param associatedJobUids: list of string (job uids)
        :param context_data:
        :param spanUid: span uid
        :return: SpanContext of the span
        """
        if uid is None:
            raise Exception('Span uid can not be None. You need to pass span uid to create span')
        create_span = Span(
            uid=uid,
            pipelineRunId=self.id
        )
        if associatedJobUids is None:
            associatedJobUids = []
        payload = self._convert_span_to_dict(create_span, associatedJobUids)
        res = self.client.create_span(self.id, payload)
        span_context = SpanContext(client=self.client, span=res, context_data= context_data, new_span = True)
        return span_context

    def get_span(self, span_uid: str):
        """
            Description:
                Get span of the pipeline run by uid
        :param span_uid: uid of the span
        :return: SpanContext instance of the input span uid
        """
        span = self.client.get_span( pipeline_run_id= self.id,uid= span_uid)
        span_context = SpanContext(client=self.client, span= span)
        return span_context

    def get_root_span(self):
        """
            Description:
                Get root span of the pipeline run
        :return: SpanContext instance of the root span
        """
        span = self.client.get_root_span( pipeline_run_id=self.id)
        span_context = SpanContext(client=self.client, span=span)
        return span_context

class Pipeline:
    def __init__(self, uid: str,
                 name: str,
                 description: str = None,
                 meta: PipelineMetadata = None,
                 createdAt: str = None,
                 enabled: bool = None,
                 id: int = None,
                 # interrupt: bool = None,
                 # notificationChannels: object = None,
                 # schedule: str = None,
                 # scheduled: bool = None,
                 # schedulerType: str = None,
                 updatedAt=None,
                 context=None,
                 client=None,
                 **kwrgs):
        """
        Description:
            Class of the pipeline
        :param uid: uid of the pipeline
        :param name: name of the pipeline
        :param description: pipeline desc
        :param meta: (PipelineMetadata)metadata of the pipeline
        :param createdAt: creation time of pipeline
        :param enabled: True if pipeline is interrupted else false
        :param id: pipeline id
        :param updatedAt: updated time of the given pipeline
        :param context: context data for the pipeline (dir)
        :param kwrgs:
        """
        self.uid = uid
        self.name = name
        self.createdAt = createdAt
        self.enabled = enabled
        self.id = id
        self.updatedAt = updatedAt
        self.description = description
        self.context = context
        if isinstance(meta, dict):
            self.meta = PipelineMetadata(**meta)
        else:
            self.meta = meta

        self.client = client

    def __eq__(self, other):
        return self.uid == other.uid

    def __repr__(self):
        return f"PipeLineResponse({self.__dict__})"

    # convert job object to dict type
    def _convert_job_to_dict(self, job: CreateJob):
        """
        Description:
            Convert createJob class instance to dict type
        :param job: createJob class instance
        :return: dict form of createJob class instance
        """
        job_dict = job.__dict__
        meta = asdict(job.meta)
        job_dict['meta'] = meta
        input_dict = []
        for ds_in in job.inputs:
            input_dict.append(asdict(ds_in, dict_factory=lambda x: {k: v for (k, v) in x if v is not None}))
        output_dict = []
        for ds_out in job.outputs:
            output_dict.append(asdict(ds_out, dict_factory=lambda x: {k: v for (k, v) in x if v is not None}))
        job_dict['inputs'] = input_dict
        job_dict['outputs'] = output_dict
        job_dict['pipelineUid'] = self.uid
        return job_dict

    # to create job for any given pipeline
    def create_job(self, job: CreateJob):
        """
        Description:
            Used to create job in a pipeline
        :param job: createJob class instance that you want to add in pipeline
        :return: Job class instance of created job
        """
        if job.uid is None or job.name is None:
            raise Exception('To create a job, job uid, name is required')

        payload = self._convert_job_to_dict(job)
        res = self.client.create_job(payload, self.id)
        return res

    # convert pipeline run to dict type
    def _convert_pipeline_run_to_dict(self, pipeline_run: PipelineRun):
        """
            Description:
                Convert PipelineRun class instance to dict type
            :param pipelineRun: PipelineRun class instance
            :return: dict form of PipelineRun class instance
        """
        payload = pipeline_run.__dict__
        payload['status'] = pipeline_run.status.name
        payload['result'] = pipeline_run.result.name
        pipeline_run_payload = {'run': payload}
        return pipeline_run_payload

    # create run for a pipeline
    def create_pipeline_run(self, context_data: {} = None, continuation_id: str = None) -> PipelineRun:
        """
        Description:
            used to create a pipeline run
        :param context_data: pipeline run argument
        :param continuation_id: continuation_id of pipeline run. Default value is None
        :return: pipelineRun class instance
        """
        create_pipeline_run = PipelineRun(
            pipelineId=self.id,
            args=context_data,
            result=PipelineRunResult.UNKNOWN,
            continuationId=continuation_id
        )
        payload = self._convert_pipeline_run_to_dict(create_pipeline_run)
        res = self.client.create_pipeline_run(payload)
        return res

    def get_latest_pipeline_run(self) -> PipelineRun:
        return self.client.get_latest_pipeline_run(pipeline_id=self.id)

    def get_pipeline_run(self, pipeline_run_id) -> PipelineRun:
        return self.client.get_pipeline_run(pipeline_run_id=pipeline_run_id)
