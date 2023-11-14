<img src="https://static.remotasks.com/uploads/602b25a6e0984c00343d3b26/scale-1.png"/>

# Scale EGP Python Client

**The official Python client for Scale's [Enterprise Generative AI Platform](https://scale.com/generative-ai-platform)**.

Generative AI applications are proliferating in the modern enterprise. However, building these applications can be challenging and expensive, especially when they need to conform to enterprise security and scalability standards. Scale EGP APIs provide the full-stack capabilities enterprises need to rapidly develop and deploy Generative AI applications for custom use cases. These capabilities include loading custom data sources, indexing data into vector stores, running inference, executing agents, and robust evaluation features.

### Install from PyPI:
```shell
pip install scale-egp
```

## Evaluation API

### Quickstart

```python
import hashlib
import json
import os
import pickle
from datetime import datetime
from typing import List, Union

import dotenv
import questionary as q

from egp.sdk.client import EGPClient
from egp.sdk.models import (
    TestCaseSchemaType,
    CategoricalChoice, CategoricalQuestion, EvaluationConfig, TestCaseResultRequest,
)
from egp.sdk.enums import TestCaseSchemaType, EvaluationType
from egp.utils.model_utils import BaseModel

ENV_FILE = "../../.env.local"
dotenv.load_dotenv(ENV_FILE, override=True)

DATASET_ID = None
APP_SPEC_ID = None
STUDIO_PROJECT_ID = None


def timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def dump_model(model: Union[BaseModel, List[BaseModel]]):
    if isinstance(model, list):
        return json.dumps([m.dict() for m in model], indent=2, sort_keys=True, default=str)
    return json.dumps(model.dict(), indent=2, sort_keys=True, default=str)


# Not part of our SDK. This is scratch code example of what a user might write as an application.
class MyGenerativeAIApplication:

    name = "AI@MS"
    description = "AI Chatbot to help Wealth Management Advisors"
    embedding_model = "openai/text-embedding-ada-002"
    llm_model = "gpt-3.5-turbo-0613"

    @staticmethod
    def generate(input: str):
        """
        This can be an arbitrarily complex AI application and can return any type of output. In
        general, you application should output the output string of the generate response and a
        JSON object containing any extra information you want annotators to see that the
        application used to generate the output.
        """
        output = f"Output for: {input}"
        extra_info = {
            "info": "This is a string",
            "schema": "string",  # Validate that this schema is something we support.
        }
        return output, extra_info

    def tags(self):
        return {
            "embedding_model": self.embedding_model,
            "llm_model": self.llm_model,
        }

    @property
    def version(self):
        """
        Returns a hash of the application state that is stable across processes.
        """
        return hashlib.sha256(pickle.dumps(self.tags)).hexdigest()


if __name__ == "__main__":
    gen_ai_app = MyGenerativeAIApplication()
    client = EGPClient()
    current_timestamp = timestamp()

    # Create a new dataset or use an existing one.
    evaluation_dataset_name = f"AI@MS Regression Test Dataset {current_timestamp}"
    if DATASET_ID:
        evaluation_dataset_id = DATASET_ID
    else:
        evaluation_dataset_id = q.text(
            f"ID of existing dataset (Leave blank to create a new one with name "
            f"'{evaluation_dataset_name}'):"
        ).ask()
    if evaluation_dataset_id:
        evaluation_dataset = client.evaluation_datasets().get(id=evaluation_dataset_id)
    else:
        evaluation_dataset = client.evaluation_datasets().create_from_file(
            name=evaluation_dataset_name,
            schema_type=TestCaseSchemaType.GENERATION,
            filepath=os.path.join(os.path.dirname(__file__), "data/golden_dataset.jsonl"),
        )
        print(
            f"Created evaluation dataset:\n{dump_model(evaluation_dataset)}"
        )

    # Create a new application spec or use an existing one.
    if APP_SPEC_ID:
        application_spec_id = APP_SPEC_ID
    else:
        application_spec_id = q.text(
            f"ID of existing application spec (Leave blank to create a new one with name "
            f"'{gen_ai_app.name}'):"
        ).ask()
    if application_spec_id:
        application_spec = client.application_specs().get(id=application_spec_id)
    else:
        application_spec = client.application_specs().create(
            name=gen_ai_app.name,
            # TODO: Make application names globally unique or at least unique per account
            description=gen_ai_app.description
        )
        print(f"Created application spec:\n{dump_model(application_spec)}")

    # Create a new studio project or use an existing one.
    studio_project_name = f"{current_timestamp}"
    if STUDIO_PROJECT_ID:
        studio_project_id = STUDIO_PROJECT_ID
    else:
        studio_project_id = q.text(
            f"ID of existing studio project (Leave blank to create a new one with name "
            f"'{studio_project_name}'):"
        ).ask()
    if studio_project_id:
        studio_project = client.studio_projects().get(id=studio_project_id)
    else:
        studio_project = client.studio_projects().create(
            name=studio_project_name,
            description="Annotation project for the AI@MS project",
            studio_api_key=os.environ.get("STUDIO_API_KEY"),
        )
        studio_project_id = studio_project.id
        print(f"Created studio project:\n{dump_model(studio_project)}")

    evaluation = client.evaluations().create(
        application_spec_id=application_spec_id,
        name=f"AI@MS Regression Test - {current_timestamp}",
        description="Evaluation of the AI@MS project against the AI@MS regression test dataset",
        tags=gen_ai_app.tags(),
        evaluation_config=EvaluationConfig(
            evaluation_type=EvaluationType.STUDIO,
            studio_project_id=studio_project.id,
            questions=[
                # For categorical questions, the value is used as a score for the answer.
                # Higher values are better. This score will be used to track if the AI is improving.
                # The value can be set to None if
                CategoricalQuestion(
                    question_id="based_on_content",
                    title="Was the answer based on the content provided?",
                    choices=[
                        CategoricalChoice(label="No", value=0),
                        CategoricalChoice(label="Yes", value=1),
                    ],
                ),
                CategoricalQuestion(
                    question_id="accurate",
                    title="Was the answer accurate?",
                    choices=[
                        CategoricalChoice(label="No", value=0),
                        CategoricalChoice(label="Yes", value=1),
                    ],
                ),
                CategoricalQuestion(
                    question_id="complete",
                    title="Was the answer complete?",
                    choices=[
                        CategoricalChoice(label="No", value=0),
                        CategoricalChoice(label="Yes", value=1),
                    ],
                ),
                CategoricalQuestion(
                    question_id="recent",
                    title="Was the information recent?",
                    choices=[
                        CategoricalChoice(label="Not Applicable", value=None),
                        CategoricalChoice(label="No", value=0),
                        CategoricalChoice(label="Yes", value=1),
                    ],
                ),
                CategoricalQuestion(
                    question_id="core_issue",
                    title="What was the core issue?",
                    choices=[
                        CategoricalChoice(label="No Issue", value=None),
                        CategoricalChoice(label="User Behavior Issue", value=None),
                        CategoricalChoice(label="Unable to Provide Response", value=None),
                        CategoricalChoice(label="Incomplete Answer", value=None),
                    ],
                ),
            ]
        ).dict(),
    )
    print(f"Created evaluation:\n{dump_model(evaluation)}")

    # Execute test cases
    # TODO: dataset.test_cases.iter() returns *all* test cases right now
    # not just the test_cases for the current dataset
    print(f"Submitting test case results for evaluation dataset:\n{evaluation_dataset.name}")
    test_case_results_batch = []
    for test_case in client.evaluation_datasets().test_cases().iter(
        evaluation_dataset_id=evaluation_dataset.id
    ):
        if test_case.evaluation_dataset_id == evaluation_dataset.id:
            output, extra_info = gen_ai_app.generate(input=test_case.test_case_data['input'])
            test_case_results_batch.append(
                TestCaseResultRequest(
                    application_spec_id=application_spec.id,
                    evaluation_dataset_id=evaluation_dataset.id,
                    test_case_version_id=test_case.version_id,
                    test_case_id=test_case.id,
                    test_case_evaluation_data_schema=TestCaseSchemaType.GENERATION,
                    test_case_evaluation_data=dict(
                        output=output,
                        output_extra_info=extra_info
                    ),
                )
            )
    test_case_results = client.evaluations().test_case_results().create_batch(
        evaluation_id=evaluation.id,
        test_case_results=test_case_results_batch,
    )
    print(f"Created {len(test_case_results)} test case results:\n{dump_model(test_case_results)}")

```


### Key Features


### Features Coming Soon


