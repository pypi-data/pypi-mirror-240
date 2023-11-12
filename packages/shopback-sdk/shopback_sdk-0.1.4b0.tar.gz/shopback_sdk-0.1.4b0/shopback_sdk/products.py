from typing import Optional

import os
from dataclasses import dataclass, field

import requests
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport


@dataclass
class ProductData:
    project_id: int
    category_name: str
    name: str
    description: str
    price: float
    attachment_ids: list[int]
    external_id: Optional[str] = None
    category_external_id: Optional[str] = None
    count: Optional[int] = None


@dataclass
class CategoryData:
    project_id: int
    name: str
    external_id: str
    is_visible: bool = True
    attachment: Optional[int] = None
    parent_external_id: Optional[int] = None


class ClientSDK:
    DEFAULT_URL = "https://shopback-prod.ru-prod2.kts.studio"

    def __init__(
        self, shopback_token: str, shopback_project: str, url: Optional[str] = None
    ) -> None:
        self.url = url or self.DEFAULT_URL
        self.shopback_token = shopback_token
        self.shopback_project = shopback_project
        t = RequestsHTTPTransport(self.graphql_url, headers=self.session_headers)
        self.client = Client(transport=t, fetch_schema_from_transport=True)

    @property
    def graphql_url(self) -> str:
        return self.url + "/graphql"

    @property
    def upload_url(self) -> str:
        return self.graphql_url + "/attachment/upload"

    @property
    def session_headers(self) -> dict:
        return {
            "X-Shopback-Token": self.shopback_token,
            "X-Shopback-Project": self.shopback_project,
        }

    def upload_files(self, paths: list[str]) -> list[int]:
        res = []
        files = [
            ("file", (os.path.basename(item), open(item, mode="rb"), "image/*")) for item in paths
        ]
        response = requests.post(self.upload_url, headers=self.session_headers, files=files)
        if response.status_code == 200:
            data = response.json()["data"]
            res += [item["aid"] for item in data]
        return res

    def upload_urls(self, urls: list[str]) -> list[Optional[int]]:
        res: list[Optional[int]] = []
        for url in urls:
            r = requests.get(url, allow_redirects=False)
            if r.status_code != 200:
                res.append(None)
                continue
            name = url.split("/")[-1]
            files = [("file", (name, r.content, "image/*"))]
            response = requests.post(self.upload_url, headers=self.session_headers, files=files)
            if response.status_code == 200:
                data = response.json()["data"]
                res += [item["aid"] for item in data]
        return res

    def upload_product(self, product: ProductData) -> dict:
        query = gql(
            """
            mutation product(
              $categoryProject: Int!,
              $categoryName: String!,
              $categoryExternalId: String,
              $externalId: String,
              $name: String!,
              $description: String!,
              $price: Decimal!,
              $count: Int,
              $attachments: [Int]!
            ) {
              product(input: {
                name: $name,
                externalId: $externalId,
                categoryProject: $categoryProject,
                description: $description,
                price: $price,
                categoryName: $categoryName,
                categoryExternalId: $categoryExternalId,
                count: $count,
                attachments: $attachments}
              ) {
                data {id},
                errors {status, message, fieldProblems {fieldName, errDescription}}
              }
            }
        """
        )
        params = {
            "name": product.name,
            "externalId": product.external_id,
            "categoryProject": product.project_id,
            "description": product.description,
            "price": product.price,
            "categoryName": product.category_name,
            "categoryExternalId": product.category_external_id,
            "attachments": product.attachment_ids,
            "count": product.count,
        }
        result = self.client.execute(query, variable_values=params)
        return result

    def upload_product_and_return_id(self, product: ProductData) -> int:
        res = self.upload_product(product)
        product_id = res["product"]["data"]["id"]
        product_id = int(product_id)
        return product_id

    def upload_category(self, category: CategoryData) -> dict:
        query = gql(
            """
            mutation category(
                $project: String!,
                $name: String,
                $externalId: String!,
                $isVisible: Boolean,
                $attachment: String,
                $parentExternalId: String
            ) {
              category(input: {
                project: $project,
                name: $name,
                externalId: $externalId,
                isVisible: $isVisible,
                attachment: $attachment,
                parentExternalId: $parentExternalId
              }) {
                data {
                  id
                },
                errors {status, message, fieldProblems {fieldName, errDescription}}
              }
            }
        """
        )
        params = {
            "project": str(category.project_id),
            "name": category.name,
            "externalId": category.external_id,
            "isVisible": category.is_visible,
            "attachment": str(category.attachment) if category.attachment else "",
            "parentExternalId": category.parent_external_id or "",
        }
        result = self.client.execute(query, variable_values=params)
        return result
