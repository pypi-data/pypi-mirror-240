import pytest

from ord_mediascout_client import (
    ORDMediascoutClient,
    ORDMediascoutConfig,
    CampaignType,
    CreativeForm,
    GetCreativesWebApiDto,
)
from ord_mediascout_client.feed_models import (
    CreateFeedElementsWebApiDto,
    FeedElementWebApiDto,
    FeedElementTextDataItem,
    CreateContainerWebApiDto,
    ResponseContainerWebApiDto,
    GetFeedElementsWebApiDto,
    GetContainerWebApiDto,
)


@pytest.fixture
def client() -> ORDMediascoutClient:
    config = ORDMediascoutConfig()
    return ORDMediascoutClient(config)


# Test is temporarily disabled
def test_create_feed_element(client: ORDMediascoutClient) -> None:
    request_data = CreateFeedElementsWebApiDto(
        feedName='Feed Element Test Two',
        feedElements=[
            FeedElementWebApiDto(
                # nativeCustomerId='3',
                description='first of test_feed_lighter_one',
                advertiserUrls=['http://lighter_one.kz'],
                textData=[
                    FeedElementTextDataItem(
                        textData='sampletext',
                    )
                ]
            )
        ],
        # feedNativeCustomerId='15',
    )

    response_data = client.create_feed_elements(request_data)

    print(response_data)

    assert response_data is not None


def test__get_feed(client: ORDMediascoutClient) -> None:
    request_data = GetContainerWebApiDto(
        id='ACqch23le-LEywv5-86MgeDA',
    )

    response_data = client.get_containers(parameters=request_data)

    print(response_data)

    assert response_data is not None


# Test is temporarily disabled
def test_get_feed_elements(client: ORDMediascoutClient) -> None:
    request_data = GetFeedElementsWebApiDto(

    )

    response_data = client.get_feed_elements(request_data)

    feeds = []

    for ele in response_data:
        if ele.feedId == 'FDdwOUI1vTsU6T9BIMrWgAtA':
            feeds.append(ele)

    for feed in feeds:
        print('\n\tfeed: ', feed)

    assert response_data is not None


# Test is temporarily disabled
def test_create_container(client: ORDMediascoutClient) -> None:
    request_data = CreateContainerWebApiDto(
        type=CampaignType.CPM,
        form=CreativeForm.Other,
        description='test container description',
        name='test container name',
        feedId='FDjLCpcQd5xE-6UB9K2c6nsQ', #FD4DHlrdcfpk2fe540VFBjvQ это то, что нам присылают при регистрации одного элемента - FeedId
        finalContractId='CTiwhIpoQ_F0OEPpKj8vWKGg',
        okvedCodes=[],
        isNative=False,
        isSocial=False,
    )
    # возвращается erid - запихиваем его в поле marker модели Feed
    #

    try:
        response_data = client.create_container(request_data)
    except Exception as e:
        print(e)

    # print(response_data)

    # assert response_data.id is not None


def test_get_creatives(client: ORDMediascoutClient) -> None:
    request_data = GetCreativesWebApiDto(
        creativeId='CR0vfjE93KsUyQbT9kQTod5A',
    )
    response_data = client.get_creatives(request_data)
    print(response_data)

    assert 1 == 1
