# -*- coding: utf-8 -*-

# Copyright (C) 2019  Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Any, Callable, Iterable

from google.cloud.billing_v1.types import cloud_billing


class ListBillingAccountsPager:
    """A pager for iterating through ``list_billing_accounts`` requests.

    This class thinly wraps an initial
    :class:`~.cloud_billing.ListBillingAccountsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``billing_accounts`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBillingAccounts`` requests and continue to iterate
    through the ``billing_accounts`` field on the
    corresponding responses.

    All the usual :class:`~.cloud_billing.ListBillingAccountsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            [cloud_billing.ListBillingAccountsRequest],
            cloud_billing.ListBillingAccountsResponse,
        ],
        request: cloud_billing.ListBillingAccountsRequest,
        response: cloud_billing.ListBillingAccountsResponse,
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.cloud_billing.ListBillingAccountsRequest`):
                The initial request object.
            response (:class:`~.cloud_billing.ListBillingAccountsResponse`):
                The initial response object.
        """
        self._method = method
        self._request = cloud_billing.ListBillingAccountsRequest(request)
        self._response = response

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[cloud_billing.ListBillingAccountsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request)
            yield self._response

    def __iter__(self) -> Iterable[cloud_billing.BillingAccount]:
        for page in self.pages:
            yield from page.billing_accounts

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProjectBillingInfoPager:
    """A pager for iterating through ``list_project_billing_info`` requests.

    This class thinly wraps an initial
    :class:`~.cloud_billing.ListProjectBillingInfoResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``project_billing_info`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProjectBillingInfo`` requests and continue to iterate
    through the ``project_billing_info`` field on the
    corresponding responses.

    All the usual :class:`~.cloud_billing.ListProjectBillingInfoResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            [cloud_billing.ListProjectBillingInfoRequest],
            cloud_billing.ListProjectBillingInfoResponse,
        ],
        request: cloud_billing.ListProjectBillingInfoRequest,
        response: cloud_billing.ListProjectBillingInfoResponse,
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.cloud_billing.ListProjectBillingInfoRequest`):
                The initial request object.
            response (:class:`~.cloud_billing.ListProjectBillingInfoResponse`):
                The initial response object.
        """
        self._method = method
        self._request = cloud_billing.ListProjectBillingInfoRequest(request)
        self._response = response

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[cloud_billing.ListProjectBillingInfoResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request)
            yield self._response

    def __iter__(self) -> Iterable[cloud_billing.ProjectBillingInfo]:
        for page in self.pages:
            yield from page.project_billing_info

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
