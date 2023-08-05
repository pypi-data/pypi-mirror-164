import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class DataAwsElasticsearchDomain(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/elasticsearch_domain aws_elasticsearch_domain}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/elasticsearch_domain aws_elasticsearch_domain} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/elasticsearch_domain#domain_name DataAwsElasticsearchDomain#domain_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/elasticsearch_domain#id DataAwsElasticsearchDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/elasticsearch_domain#tags DataAwsElasticsearchDomain#tags}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomain.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsElasticsearchDomainConfig(
            domain_name=domain_name,
            id=id,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessPolicies")
    def access_policies(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessPolicies"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="advancedOptions")
    def advanced_options(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "advancedOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="advancedSecurityOptions")
    def advanced_security_options(
        self,
    ) -> "DataAwsElasticsearchDomainAdvancedSecurityOptionsList":
        return typing.cast("DataAwsElasticsearchDomainAdvancedSecurityOptionsList", jsii.get(self, "advancedSecurityOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoTuneOptions")
    def auto_tune_options(self) -> "DataAwsElasticsearchDomainAutoTuneOptionsList":
        return typing.cast("DataAwsElasticsearchDomainAutoTuneOptionsList", jsii.get(self, "autoTuneOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterConfig")
    def cluster_config(self) -> "DataAwsElasticsearchDomainClusterConfigList":
        return typing.cast("DataAwsElasticsearchDomainClusterConfigList", jsii.get(self, "clusterConfig"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cognitoOptions")
    def cognito_options(self) -> "DataAwsElasticsearchDomainCognitoOptionsList":
        return typing.cast("DataAwsElasticsearchDomainCognitoOptionsList", jsii.get(self, "cognitoOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="created")
    def created(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "created"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deleted")
    def deleted(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "deleted"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ebsOptions")
    def ebs_options(self) -> "DataAwsElasticsearchDomainEbsOptionsList":
        return typing.cast("DataAwsElasticsearchDomainEbsOptionsList", jsii.get(self, "ebsOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="elasticsearchVersion")
    def elasticsearch_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticsearchVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionAtRest")
    def encryption_at_rest(self) -> "DataAwsElasticsearchDomainEncryptionAtRestList":
        return typing.cast("DataAwsElasticsearchDomainEncryptionAtRestList", jsii.get(self, "encryptionAtRest"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kibanaEndpoint")
    def kibana_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kibanaEndpoint"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logPublishingOptions")
    def log_publishing_options(
        self,
    ) -> "DataAwsElasticsearchDomainLogPublishingOptionsList":
        return typing.cast("DataAwsElasticsearchDomainLogPublishingOptionsList", jsii.get(self, "logPublishingOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nodeToNodeEncryption")
    def node_to_node_encryption(
        self,
    ) -> "DataAwsElasticsearchDomainNodeToNodeEncryptionList":
        return typing.cast("DataAwsElasticsearchDomainNodeToNodeEncryptionList", jsii.get(self, "nodeToNodeEncryption"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="processing")
    def processing(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "processing"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshotOptions")
    def snapshot_options(self) -> "DataAwsElasticsearchDomainSnapshotOptionsList":
        return typing.cast("DataAwsElasticsearchDomainSnapshotOptionsList", jsii.get(self, "snapshotOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcOptions")
    def vpc_options(self) -> "DataAwsElasticsearchDomainVpcOptionsList":
        return typing.cast("DataAwsElasticsearchDomainVpcOptionsList", jsii.get(self, "vpcOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomain, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomain, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomain, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAdvancedSecurityOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainAdvancedSecurityOptions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainAdvancedSecurityOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainAdvancedSecurityOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAdvancedSecurityOptionsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAdvancedSecurityOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainAdvancedSecurityOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAdvancedSecurityOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainAdvancedSecurityOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAdvancedSecurityOptionsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAdvancedSecurityOptionsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAdvancedSecurityOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainAdvancedSecurityOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAdvancedSecurityOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAdvancedSecurityOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalUserDatabaseEnabled")
    def internal_user_database_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "internalUserDatabaseEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainAdvancedSecurityOptions]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainAdvancedSecurityOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainAdvancedSecurityOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAdvancedSecurityOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAutoTuneOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainAutoTuneOptions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainAutoTuneOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainAutoTuneOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAutoTuneOptionsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAutoTuneOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainAutoTuneOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAutoTuneOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainAutoTuneOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceSchedule",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceSchedule:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cronExpressionForRecurrence")
    def cron_expression_for_recurrence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cronExpressionForRecurrence"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="duration")
    def duration(
        self,
    ) -> DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationList:
        return typing.cast(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationList, jsii.get(self, "duration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="startAt")
    def start_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsElasticsearchDomainAutoTuneOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainAutoTuneOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainAutoTuneOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maintenanceSchedule")
    def maintenance_schedule(
        self,
    ) -> DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList:
        return typing.cast(DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList, jsii.get(self, "maintenanceSchedule"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rollbackOnDisable")
    def rollback_on_disable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rollbackOnDisable"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainAutoTuneOptions]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainAutoTuneOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainAutoTuneOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainAutoTuneOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainClusterConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainClusterConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainClusterConfigColdStorageOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainClusterConfigColdStorageOptions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainClusterConfigColdStorageOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainClusterConfigColdStorageOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainClusterConfigColdStorageOptionsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainClusterConfigColdStorageOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainClusterConfigColdStorageOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainClusterConfigColdStorageOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainClusterConfigColdStorageOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigColdStorageOptionsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigColdStorageOptionsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigColdStorageOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainClusterConfigColdStorageOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainClusterConfigColdStorageOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainClusterConfigColdStorageOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainClusterConfigColdStorageOptions]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainClusterConfigColdStorageOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainClusterConfigColdStorageOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigColdStorageOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsElasticsearchDomainClusterConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainClusterConfigList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainClusterConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainClusterConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainClusterConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainClusterConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainClusterConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="coldStorageOptions")
    def cold_storage_options(
        self,
    ) -> DataAwsElasticsearchDomainClusterConfigColdStorageOptionsList:
        return typing.cast(DataAwsElasticsearchDomainClusterConfigColdStorageOptionsList, jsii.get(self, "coldStorageOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedMasterCount")
    def dedicated_master_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dedicatedMasterCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedMasterEnabled")
    def dedicated_master_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "dedicatedMasterEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedMasterType")
    def dedicated_master_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dedicatedMasterType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="warmCount")
    def warm_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "warmCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="warmEnabled")
    def warm_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "warmEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="warmType")
    def warm_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warmType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="zoneAwarenessConfig")
    def zone_awareness_config(
        self,
    ) -> "DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigList":
        return typing.cast("DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigList", jsii.get(self, "zoneAwarenessConfig"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="zoneAwarenessEnabled")
    def zone_awareness_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "zoneAwarenessEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainClusterConfig]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZoneCount")
    def availability_zone_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "availabilityZoneCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfig]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainCognitoOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainCognitoOptions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainCognitoOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainCognitoOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainCognitoOptionsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainCognitoOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainCognitoOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainCognitoOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainCognitoOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainCognitoOptionsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainCognitoOptionsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainCognitoOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainCognitoOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainCognitoOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainCognitoOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityPoolId")
    def identity_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityPoolId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainCognitoOptions]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainCognitoOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainCognitoOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainCognitoOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain_name": "domainName",
        "id": "id",
        "tags": "tags",
    },
)
class DataAwsElasticsearchDomainConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]] = None,
        domain_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS ElasticSearch Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/elasticsearch_domain#domain_name DataAwsElasticsearchDomain#domain_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/elasticsearch_domain#id DataAwsElasticsearchDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/elasticsearch_domain#tags DataAwsElasticsearchDomain#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]], result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/elasticsearch_domain#domain_name DataAwsElasticsearchDomain#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/elasticsearch_domain#id DataAwsElasticsearchDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/elasticsearch_domain#tags DataAwsElasticsearchDomain#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainEbsOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainEbsOptions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainEbsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainEbsOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainEbsOptionsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainEbsOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainEbsOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainEbsOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainEbsOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainEbsOptionsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainEbsOptionsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainEbsOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainEbsOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainEbsOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainEbsOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ebsEnabled")
    def ebs_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "ebsEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsElasticsearchDomainEbsOptions]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainEbsOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainEbsOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainEbsOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainEncryptionAtRest",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainEncryptionAtRest:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainEncryptionAtRest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainEncryptionAtRestList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainEncryptionAtRestList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainEncryptionAtRestList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainEncryptionAtRestOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainEncryptionAtRestList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainEncryptionAtRestOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainEncryptionAtRestList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainEncryptionAtRestList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainEncryptionAtRestList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainEncryptionAtRestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainEncryptionAtRestOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainEncryptionAtRestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainEncryptionAtRest]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainEncryptionAtRest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainEncryptionAtRest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainEncryptionAtRestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainLogPublishingOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainLogPublishingOptions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainLogPublishingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainLogPublishingOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainLogPublishingOptionsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainLogPublishingOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainLogPublishingOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainLogPublishingOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainLogPublishingOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainLogPublishingOptionsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainLogPublishingOptionsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainLogPublishingOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainLogPublishingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainLogPublishingOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainLogPublishingOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLogGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logType")
    def log_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainLogPublishingOptions]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainLogPublishingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainLogPublishingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainLogPublishingOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainNodeToNodeEncryption",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainNodeToNodeEncryption:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainNodeToNodeEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainNodeToNodeEncryptionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainNodeToNodeEncryptionList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainNodeToNodeEncryptionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainNodeToNodeEncryptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainNodeToNodeEncryptionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainNodeToNodeEncryptionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainNodeToNodeEncryptionList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainNodeToNodeEncryptionList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainNodeToNodeEncryptionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainNodeToNodeEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainNodeToNodeEncryptionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainNodeToNodeEncryptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainNodeToNodeEncryption]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainNodeToNodeEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainNodeToNodeEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainNodeToNodeEncryptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainSnapshotOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainSnapshotOptions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainSnapshotOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainSnapshotOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainSnapshotOptionsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainSnapshotOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainSnapshotOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainSnapshotOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainSnapshotOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainSnapshotOptionsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainSnapshotOptionsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainSnapshotOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainSnapshotOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainSnapshotOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainSnapshotOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="automatedSnapshotStartHour")
    def automated_snapshot_start_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "automatedSnapshotStartHour"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsElasticsearchDomainSnapshotOptions]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainSnapshotOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainSnapshotOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainSnapshotOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainVpcOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsElasticsearchDomainVpcOptions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsElasticsearchDomainVpcOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsElasticsearchDomainVpcOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainVpcOptionsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainVpcOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsElasticsearchDomainVpcOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainVpcOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsElasticsearchDomainVpcOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainVpcOptionsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainVpcOptionsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainVpcOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsElasticsearchDomainVpcOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.DataAwsElasticsearchDomainVpcOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsElasticsearchDomainVpcOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsElasticsearchDomainVpcOptions]:
        return typing.cast(typing.Optional[DataAwsElasticsearchDomainVpcOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsElasticsearchDomainVpcOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsElasticsearchDomainVpcOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomain(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain aws_elasticsearch_domain}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        access_policies: typing.Optional[builtins.str] = None,
        advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        advanced_security_options: typing.Optional[typing.Union["ElasticsearchDomainAdvancedSecurityOptions", typing.Dict[str, typing.Any]]] = None,
        auto_tune_options: typing.Optional[typing.Union["ElasticsearchDomainAutoTuneOptions", typing.Dict[str, typing.Any]]] = None,
        cluster_config: typing.Optional[typing.Union["ElasticsearchDomainClusterConfig", typing.Dict[str, typing.Any]]] = None,
        cognito_options: typing.Optional[typing.Union["ElasticsearchDomainCognitoOptions", typing.Dict[str, typing.Any]]] = None,
        domain_endpoint_options: typing.Optional[typing.Union["ElasticsearchDomainDomainEndpointOptions", typing.Dict[str, typing.Any]]] = None,
        ebs_options: typing.Optional[typing.Union["ElasticsearchDomainEbsOptions", typing.Dict[str, typing.Any]]] = None,
        elasticsearch_version: typing.Optional[builtins.str] = None,
        encrypt_at_rest: typing.Optional[typing.Union["ElasticsearchDomainEncryptAtRest", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        log_publishing_options: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElasticsearchDomainLogPublishingOptions", typing.Dict[str, typing.Any]]]]] = None,
        node_to_node_encryption: typing.Optional[typing.Union["ElasticsearchDomainNodeToNodeEncryption", typing.Dict[str, typing.Any]]] = None,
        snapshot_options: typing.Optional[typing.Union["ElasticsearchDomainSnapshotOptions", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ElasticsearchDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpc_options: typing.Optional[typing.Union["ElasticsearchDomainVpcOptions", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain aws_elasticsearch_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_name ElasticsearchDomain#domain_name}.
        :param access_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#access_policies ElasticsearchDomain#access_policies}.
        :param advanced_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_options ElasticsearchDomain#advanced_options}.
        :param advanced_security_options: advanced_security_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_security_options ElasticsearchDomain#advanced_security_options}
        :param auto_tune_options: auto_tune_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#auto_tune_options ElasticsearchDomain#auto_tune_options}
        :param cluster_config: cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cluster_config ElasticsearchDomain#cluster_config}
        :param cognito_options: cognito_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cognito_options ElasticsearchDomain#cognito_options}
        :param domain_endpoint_options: domain_endpoint_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_endpoint_options ElasticsearchDomain#domain_endpoint_options}
        :param ebs_options: ebs_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_options ElasticsearchDomain#ebs_options}
        :param elasticsearch_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#elasticsearch_version ElasticsearchDomain#elasticsearch_version}.
        :param encrypt_at_rest: encrypt_at_rest block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#encrypt_at_rest ElasticsearchDomain#encrypt_at_rest}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#id ElasticsearchDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_publishing_options: log_publishing_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#log_publishing_options ElasticsearchDomain#log_publishing_options}
        :param node_to_node_encryption: node_to_node_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#node_to_node_encryption ElasticsearchDomain#node_to_node_encryption}
        :param snapshot_options: snapshot_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#snapshot_options ElasticsearchDomain#snapshot_options}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags ElasticsearchDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags_all ElasticsearchDomain#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#timeouts ElasticsearchDomain#timeouts}
        :param vpc_options: vpc_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#vpc_options ElasticsearchDomain#vpc_options}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomain.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElasticsearchDomainConfig(
            domain_name=domain_name,
            access_policies=access_policies,
            advanced_options=advanced_options,
            advanced_security_options=advanced_security_options,
            auto_tune_options=auto_tune_options,
            cluster_config=cluster_config,
            cognito_options=cognito_options,
            domain_endpoint_options=domain_endpoint_options,
            ebs_options=ebs_options,
            elasticsearch_version=elasticsearch_version,
            encrypt_at_rest=encrypt_at_rest,
            id=id,
            log_publishing_options=log_publishing_options,
            node_to_node_encryption=node_to_node_encryption,
            snapshot_options=snapshot_options,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            vpc_options=vpc_options,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdvancedSecurityOptions")
    def put_advanced_security_options(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        master_user_options: typing.Optional[typing.Union["ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        :param internal_user_database_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#internal_user_database_enabled ElasticsearchDomain#internal_user_database_enabled}.
        :param master_user_options: master_user_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_options ElasticsearchDomain#master_user_options}
        '''
        value = ElasticsearchDomainAdvancedSecurityOptions(
            enabled=enabled,
            internal_user_database_enabled=internal_user_database_enabled,
            master_user_options=master_user_options,
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedSecurityOptions", [value]))

    @jsii.member(jsii_name="putAutoTuneOptions")
    def put_auto_tune_options(
        self,
        *,
        desired_state: builtins.str,
        maintenance_schedule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule", typing.Dict[str, typing.Any]]]]] = None,
        rollback_on_disable: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#desired_state ElasticsearchDomain#desired_state}.
        :param maintenance_schedule: maintenance_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#maintenance_schedule ElasticsearchDomain#maintenance_schedule}
        :param rollback_on_disable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#rollback_on_disable ElasticsearchDomain#rollback_on_disable}.
        '''
        value = ElasticsearchDomainAutoTuneOptions(
            desired_state=desired_state,
            maintenance_schedule=maintenance_schedule,
            rollback_on_disable=rollback_on_disable,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoTuneOptions", [value]))

    @jsii.member(jsii_name="putClusterConfig")
    def put_cluster_config(
        self,
        *,
        cold_storage_options: typing.Optional[typing.Union["ElasticsearchDomainClusterConfigColdStorageOptions", typing.Dict[str, typing.Any]]] = None,
        dedicated_master_count: typing.Optional[jsii.Number] = None,
        dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dedicated_master_type: typing.Optional[builtins.str] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        instance_type: typing.Optional[builtins.str] = None,
        warm_count: typing.Optional[jsii.Number] = None,
        warm_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        warm_type: typing.Optional[builtins.str] = None,
        zone_awareness_config: typing.Optional[typing.Union["ElasticsearchDomainClusterConfigZoneAwarenessConfig", typing.Dict[str, typing.Any]]] = None,
        zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cold_storage_options: cold_storage_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cold_storage_options ElasticsearchDomain#cold_storage_options}
        :param dedicated_master_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_count ElasticsearchDomain#dedicated_master_count}.
        :param dedicated_master_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_enabled ElasticsearchDomain#dedicated_master_enabled}.
        :param dedicated_master_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_type ElasticsearchDomain#dedicated_master_type}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_count ElasticsearchDomain#instance_count}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_type ElasticsearchDomain#instance_type}.
        :param warm_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_count ElasticsearchDomain#warm_count}.
        :param warm_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_enabled ElasticsearchDomain#warm_enabled}.
        :param warm_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_type ElasticsearchDomain#warm_type}.
        :param zone_awareness_config: zone_awareness_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_config ElasticsearchDomain#zone_awareness_config}
        :param zone_awareness_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_enabled ElasticsearchDomain#zone_awareness_enabled}.
        '''
        value = ElasticsearchDomainClusterConfig(
            cold_storage_options=cold_storage_options,
            dedicated_master_count=dedicated_master_count,
            dedicated_master_enabled=dedicated_master_enabled,
            dedicated_master_type=dedicated_master_type,
            instance_count=instance_count,
            instance_type=instance_type,
            warm_count=warm_count,
            warm_enabled=warm_enabled,
            warm_type=warm_type,
            zone_awareness_config=zone_awareness_config,
            zone_awareness_enabled=zone_awareness_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putClusterConfig", [value]))

    @jsii.member(jsii_name="putCognitoOptions")
    def put_cognito_options(
        self,
        *,
        identity_pool_id: builtins.str,
        role_arn: builtins.str,
        user_pool_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param identity_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#identity_pool_id ElasticsearchDomain#identity_pool_id}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#role_arn ElasticsearchDomain#role_arn}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#user_pool_id ElasticsearchDomain#user_pool_id}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        value = ElasticsearchDomainCognitoOptions(
            identity_pool_id=identity_pool_id,
            role_arn=role_arn,
            user_pool_id=user_pool_id,
            enabled=enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putCognitoOptions", [value]))

    @jsii.member(jsii_name="putDomainEndpointOptions")
    def put_domain_endpoint_options(
        self,
        *,
        custom_endpoint: typing.Optional[builtins.str] = None,
        custom_endpoint_certificate_arn: typing.Optional[builtins.str] = None,
        custom_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enforce_https: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_security_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint ElasticsearchDomain#custom_endpoint}.
        :param custom_endpoint_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_certificate_arn ElasticsearchDomain#custom_endpoint_certificate_arn}.
        :param custom_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_enabled ElasticsearchDomain#custom_endpoint_enabled}.
        :param enforce_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enforce_https ElasticsearchDomain#enforce_https}.
        :param tls_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tls_security_policy ElasticsearchDomain#tls_security_policy}.
        '''
        value = ElasticsearchDomainDomainEndpointOptions(
            custom_endpoint=custom_endpoint,
            custom_endpoint_certificate_arn=custom_endpoint_certificate_arn,
            custom_endpoint_enabled=custom_endpoint_enabled,
            enforce_https=enforce_https,
            tls_security_policy=tls_security_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putDomainEndpointOptions", [value]))

    @jsii.member(jsii_name="putEbsOptions")
    def put_ebs_options(
        self,
        *,
        ebs_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ebs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_enabled ElasticsearchDomain#ebs_enabled}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#iops ElasticsearchDomain#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#throughput ElasticsearchDomain#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_size ElasticsearchDomain#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_type ElasticsearchDomain#volume_type}.
        '''
        value = ElasticsearchDomainEbsOptions(
            ebs_enabled=ebs_enabled,
            iops=iops,
            throughput=throughput,
            volume_size=volume_size,
            volume_type=volume_type,
        )

        return typing.cast(None, jsii.invoke(self, "putEbsOptions", [value]))

    @jsii.member(jsii_name="putEncryptAtRest")
    def put_encrypt_at_rest(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#kms_key_id ElasticsearchDomain#kms_key_id}.
        '''
        value = ElasticsearchDomainEncryptAtRest(
            enabled=enabled, kms_key_id=kms_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptAtRest", [value]))

    @jsii.member(jsii_name="putLogPublishingOptions")
    def put_log_publishing_options(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElasticsearchDomainLogPublishingOptions", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomain.put_log_publishing_options)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogPublishingOptions", [value]))

    @jsii.member(jsii_name="putNodeToNodeEncryption")
    def put_node_to_node_encryption(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        value = ElasticsearchDomainNodeToNodeEncryption(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putNodeToNodeEncryption", [value]))

    @jsii.member(jsii_name="putSnapshotOptions")
    def put_snapshot_options(
        self,
        *,
        automated_snapshot_start_hour: jsii.Number,
    ) -> None:
        '''
        :param automated_snapshot_start_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#automated_snapshot_start_hour ElasticsearchDomain#automated_snapshot_start_hour}.
        '''
        value = ElasticsearchDomainSnapshotOptions(
            automated_snapshot_start_hour=automated_snapshot_start_hour
        )

        return typing.cast(None, jsii.invoke(self, "putSnapshotOptions", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#create ElasticsearchDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#delete ElasticsearchDomain#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#update ElasticsearchDomain#update}.
        '''
        value = ElasticsearchDomainTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVpcOptions")
    def put_vpc_options(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#security_group_ids ElasticsearchDomain#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#subnet_ids ElasticsearchDomain#subnet_ids}.
        '''
        value = ElasticsearchDomainVpcOptions(
            security_group_ids=security_group_ids, subnet_ids=subnet_ids
        )

        return typing.cast(None, jsii.invoke(self, "putVpcOptions", [value]))

    @jsii.member(jsii_name="resetAccessPolicies")
    def reset_access_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessPolicies", []))

    @jsii.member(jsii_name="resetAdvancedOptions")
    def reset_advanced_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedOptions", []))

    @jsii.member(jsii_name="resetAdvancedSecurityOptions")
    def reset_advanced_security_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedSecurityOptions", []))

    @jsii.member(jsii_name="resetAutoTuneOptions")
    def reset_auto_tune_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoTuneOptions", []))

    @jsii.member(jsii_name="resetClusterConfig")
    def reset_cluster_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterConfig", []))

    @jsii.member(jsii_name="resetCognitoOptions")
    def reset_cognito_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCognitoOptions", []))

    @jsii.member(jsii_name="resetDomainEndpointOptions")
    def reset_domain_endpoint_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainEndpointOptions", []))

    @jsii.member(jsii_name="resetEbsOptions")
    def reset_ebs_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsOptions", []))

    @jsii.member(jsii_name="resetElasticsearchVersion")
    def reset_elasticsearch_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearchVersion", []))

    @jsii.member(jsii_name="resetEncryptAtRest")
    def reset_encrypt_at_rest(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptAtRest", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogPublishingOptions")
    def reset_log_publishing_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogPublishingOptions", []))

    @jsii.member(jsii_name="resetNodeToNodeEncryption")
    def reset_node_to_node_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeToNodeEncryption", []))

    @jsii.member(jsii_name="resetSnapshotOptions")
    def reset_snapshot_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotOptions", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpcOptions")
    def reset_vpc_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcOptions", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="advancedSecurityOptions")
    def advanced_security_options(
        self,
    ) -> "ElasticsearchDomainAdvancedSecurityOptionsOutputReference":
        return typing.cast("ElasticsearchDomainAdvancedSecurityOptionsOutputReference", jsii.get(self, "advancedSecurityOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoTuneOptions")
    def auto_tune_options(self) -> "ElasticsearchDomainAutoTuneOptionsOutputReference":
        return typing.cast("ElasticsearchDomainAutoTuneOptionsOutputReference", jsii.get(self, "autoTuneOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterConfig")
    def cluster_config(self) -> "ElasticsearchDomainClusterConfigOutputReference":
        return typing.cast("ElasticsearchDomainClusterConfigOutputReference", jsii.get(self, "clusterConfig"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cognitoOptions")
    def cognito_options(self) -> "ElasticsearchDomainCognitoOptionsOutputReference":
        return typing.cast("ElasticsearchDomainCognitoOptionsOutputReference", jsii.get(self, "cognitoOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainEndpointOptions")
    def domain_endpoint_options(
        self,
    ) -> "ElasticsearchDomainDomainEndpointOptionsOutputReference":
        return typing.cast("ElasticsearchDomainDomainEndpointOptionsOutputReference", jsii.get(self, "domainEndpointOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ebsOptions")
    def ebs_options(self) -> "ElasticsearchDomainEbsOptionsOutputReference":
        return typing.cast("ElasticsearchDomainEbsOptionsOutputReference", jsii.get(self, "ebsOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptAtRest")
    def encrypt_at_rest(self) -> "ElasticsearchDomainEncryptAtRestOutputReference":
        return typing.cast("ElasticsearchDomainEncryptAtRestOutputReference", jsii.get(self, "encryptAtRest"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kibanaEndpoint")
    def kibana_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kibanaEndpoint"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logPublishingOptions")
    def log_publishing_options(self) -> "ElasticsearchDomainLogPublishingOptionsList":
        return typing.cast("ElasticsearchDomainLogPublishingOptionsList", jsii.get(self, "logPublishingOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nodeToNodeEncryption")
    def node_to_node_encryption(
        self,
    ) -> "ElasticsearchDomainNodeToNodeEncryptionOutputReference":
        return typing.cast("ElasticsearchDomainNodeToNodeEncryptionOutputReference", jsii.get(self, "nodeToNodeEncryption"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshotOptions")
    def snapshot_options(self) -> "ElasticsearchDomainSnapshotOptionsOutputReference":
        return typing.cast("ElasticsearchDomainSnapshotOptionsOutputReference", jsii.get(self, "snapshotOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ElasticsearchDomainTimeoutsOutputReference":
        return typing.cast("ElasticsearchDomainTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcOptions")
    def vpc_options(self) -> "ElasticsearchDomainVpcOptionsOutputReference":
        return typing.cast("ElasticsearchDomainVpcOptionsOutputReference", jsii.get(self, "vpcOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessPoliciesInput")
    def access_policies_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessPoliciesInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="advancedOptionsInput")
    def advanced_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "advancedOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="advancedSecurityOptionsInput")
    def advanced_security_options_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainAdvancedSecurityOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainAdvancedSecurityOptions"], jsii.get(self, "advancedSecurityOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoTuneOptionsInput")
    def auto_tune_options_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainAutoTuneOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainAutoTuneOptions"], jsii.get(self, "autoTuneOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterConfigInput")
    def cluster_config_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainClusterConfig"]:
        return typing.cast(typing.Optional["ElasticsearchDomainClusterConfig"], jsii.get(self, "clusterConfigInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cognitoOptionsInput")
    def cognito_options_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainCognitoOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainCognitoOptions"], jsii.get(self, "cognitoOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainEndpointOptionsInput")
    def domain_endpoint_options_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainDomainEndpointOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainDomainEndpointOptions"], jsii.get(self, "domainEndpointOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ebsOptionsInput")
    def ebs_options_input(self) -> typing.Optional["ElasticsearchDomainEbsOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainEbsOptions"], jsii.get(self, "ebsOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="elasticsearchVersionInput")
    def elasticsearch_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elasticsearchVersionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptAtRestInput")
    def encrypt_at_rest_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainEncryptAtRest"]:
        return typing.cast(typing.Optional["ElasticsearchDomainEncryptAtRest"], jsii.get(self, "encryptAtRestInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logPublishingOptionsInput")
    def log_publishing_options_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElasticsearchDomainLogPublishingOptions"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElasticsearchDomainLogPublishingOptions"]]], jsii.get(self, "logPublishingOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nodeToNodeEncryptionInput")
    def node_to_node_encryption_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainNodeToNodeEncryption"]:
        return typing.cast(typing.Optional["ElasticsearchDomainNodeToNodeEncryption"], jsii.get(self, "nodeToNodeEncryptionInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshotOptionsInput")
    def snapshot_options_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainSnapshotOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainSnapshotOptions"], jsii.get(self, "snapshotOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ElasticsearchDomainTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ElasticsearchDomainTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcOptionsInput")
    def vpc_options_input(self) -> typing.Optional["ElasticsearchDomainVpcOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainVpcOptions"], jsii.get(self, "vpcOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessPolicies")
    def access_policies(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessPolicies"))

    @access_policies.setter
    def access_policies(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomain, "access_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPolicies", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="advancedOptions")
    def advanced_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "advancedOptions"))

    @advanced_options.setter
    def advanced_options(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomain, "advanced_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomain, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="elasticsearchVersion")
    def elasticsearch_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticsearchVersion"))

    @elasticsearch_version.setter
    def elasticsearch_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomain, "elasticsearch_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticsearchVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomain, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomain, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomain, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainAdvancedSecurityOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "internal_user_database_enabled": "internalUserDatabaseEnabled",
        "master_user_options": "masterUserOptions",
    },
)
class ElasticsearchDomainAdvancedSecurityOptions:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        master_user_options: typing.Optional[typing.Union["ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        :param internal_user_database_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#internal_user_database_enabled ElasticsearchDomain#internal_user_database_enabled}.
        :param master_user_options: master_user_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_options ElasticsearchDomain#master_user_options}
        '''
        if isinstance(master_user_options, dict):
            master_user_options = ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions(**master_user_options)
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAdvancedSecurityOptions.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument internal_user_database_enabled", value=internal_user_database_enabled, expected_type=type_hints["internal_user_database_enabled"])
            check_type(argname="argument master_user_options", value=master_user_options, expected_type=type_hints["master_user_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if internal_user_database_enabled is not None:
            self._values["internal_user_database_enabled"] = internal_user_database_enabled
        if master_user_options is not None:
            self._values["master_user_options"] = master_user_options

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def internal_user_database_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#internal_user_database_enabled ElasticsearchDomain#internal_user_database_enabled}.'''
        result = self._values.get("internal_user_database_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def master_user_options(
        self,
    ) -> typing.Optional["ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions"]:
        '''master_user_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_options ElasticsearchDomain#master_user_options}
        '''
        result = self._values.get("master_user_options")
        return typing.cast(typing.Optional["ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainAdvancedSecurityOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions",
    jsii_struct_bases=[],
    name_mapping={
        "master_user_arn": "masterUserArn",
        "master_user_name": "masterUserName",
        "master_user_password": "masterUserPassword",
    },
)
class ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions:
    def __init__(
        self,
        *,
        master_user_arn: typing.Optional[builtins.str] = None,
        master_user_name: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param master_user_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_arn ElasticsearchDomain#master_user_arn}.
        :param master_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_name ElasticsearchDomain#master_user_name}.
        :param master_user_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_password ElasticsearchDomain#master_user_password}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions.__init__)
            check_type(argname="argument master_user_arn", value=master_user_arn, expected_type=type_hints["master_user_arn"])
            check_type(argname="argument master_user_name", value=master_user_name, expected_type=type_hints["master_user_name"])
            check_type(argname="argument master_user_password", value=master_user_password, expected_type=type_hints["master_user_password"])
        self._values: typing.Dict[str, typing.Any] = {}
        if master_user_arn is not None:
            self._values["master_user_arn"] = master_user_arn
        if master_user_name is not None:
            self._values["master_user_name"] = master_user_name
        if master_user_password is not None:
            self._values["master_user_password"] = master_user_password

    @builtins.property
    def master_user_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_arn ElasticsearchDomain#master_user_arn}.'''
        result = self._values.get("master_user_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_name ElasticsearchDomain#master_user_name}.'''
        result = self._values.get("master_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_password ElasticsearchDomain#master_user_password}.'''
        result = self._values.get("master_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMasterUserArn")
    def reset_master_user_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterUserArn", []))

    @jsii.member(jsii_name="resetMasterUserName")
    def reset_master_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterUserName", []))

    @jsii.member(jsii_name="resetMasterUserPassword")
    def reset_master_user_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterUserPassword", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserArnInput")
    def master_user_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUserArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserNameInput")
    def master_user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUserNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserPasswordInput")
    def master_user_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUserPasswordInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserArn")
    def master_user_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterUserArn"))

    @master_user_arn.setter
    def master_user_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference, "master_user_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserName")
    def master_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterUserName"))

    @master_user_name.setter
    def master_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference, "master_user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterUserPassword"))

    @master_user_password.setter
    def master_user_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference, "master_user_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserPassword", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainAdvancedSecurityOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainAdvancedSecurityOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAdvancedSecurityOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMasterUserOptions")
    def put_master_user_options(
        self,
        *,
        master_user_arn: typing.Optional[builtins.str] = None,
        master_user_name: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param master_user_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_arn ElasticsearchDomain#master_user_arn}.
        :param master_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_name ElasticsearchDomain#master_user_name}.
        :param master_user_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_password ElasticsearchDomain#master_user_password}.
        '''
        value = ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions(
            master_user_arn=master_user_arn,
            master_user_name=master_user_name,
            master_user_password=master_user_password,
        )

        return typing.cast(None, jsii.invoke(self, "putMasterUserOptions", [value]))

    @jsii.member(jsii_name="resetInternalUserDatabaseEnabled")
    def reset_internal_user_database_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalUserDatabaseEnabled", []))

    @jsii.member(jsii_name="resetMasterUserOptions")
    def reset_master_user_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterUserOptions", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserOptions")
    def master_user_options(
        self,
    ) -> ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference:
        return typing.cast(ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference, jsii.get(self, "masterUserOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalUserDatabaseEnabledInput")
    def internal_user_database_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "internalUserDatabaseEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserOptionsInput")
    def master_user_options_input(
        self,
    ) -> typing.Optional[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions], jsii.get(self, "masterUserOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAdvancedSecurityOptionsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalUserDatabaseEnabled")
    def internal_user_database_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "internalUserDatabaseEnabled"))

    @internal_user_database_enabled.setter
    def internal_user_database_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAdvancedSecurityOptionsOutputReference, "internal_user_database_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalUserDatabaseEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainAdvancedSecurityOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainAdvancedSecurityOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainAdvancedSecurityOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAdvancedSecurityOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainAutoTuneOptions",
    jsii_struct_bases=[],
    name_mapping={
        "desired_state": "desiredState",
        "maintenance_schedule": "maintenanceSchedule",
        "rollback_on_disable": "rollbackOnDisable",
    },
)
class ElasticsearchDomainAutoTuneOptions:
    def __init__(
        self,
        *,
        desired_state: builtins.str,
        maintenance_schedule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule", typing.Dict[str, typing.Any]]]]] = None,
        rollback_on_disable: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#desired_state ElasticsearchDomain#desired_state}.
        :param maintenance_schedule: maintenance_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#maintenance_schedule ElasticsearchDomain#maintenance_schedule}
        :param rollback_on_disable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#rollback_on_disable ElasticsearchDomain#rollback_on_disable}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAutoTuneOptions.__init__)
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument maintenance_schedule", value=maintenance_schedule, expected_type=type_hints["maintenance_schedule"])
            check_type(argname="argument rollback_on_disable", value=rollback_on_disable, expected_type=type_hints["rollback_on_disable"])
        self._values: typing.Dict[str, typing.Any] = {
            "desired_state": desired_state,
        }
        if maintenance_schedule is not None:
            self._values["maintenance_schedule"] = maintenance_schedule
        if rollback_on_disable is not None:
            self._values["rollback_on_disable"] = rollback_on_disable

    @builtins.property
    def desired_state(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#desired_state ElasticsearchDomain#desired_state}.'''
        result = self._values.get("desired_state")
        assert result is not None, "Required property 'desired_state' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def maintenance_schedule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule"]]]:
        '''maintenance_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#maintenance_schedule ElasticsearchDomain#maintenance_schedule}
        '''
        result = self._values.get("maintenance_schedule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule"]]], result)

    @builtins.property
    def rollback_on_disable(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#rollback_on_disable ElasticsearchDomain#rollback_on_disable}.'''
        result = self._values.get("rollback_on_disable")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainAutoTuneOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "cron_expression_for_recurrence": "cronExpressionForRecurrence",
        "duration": "duration",
        "start_at": "startAt",
    },
)
class ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule:
    def __init__(
        self,
        *,
        cron_expression_for_recurrence: builtins.str,
        duration: typing.Union["ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration", typing.Dict[str, typing.Any]],
        start_at: builtins.str,
    ) -> None:
        '''
        :param cron_expression_for_recurrence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cron_expression_for_recurrence ElasticsearchDomain#cron_expression_for_recurrence}.
        :param duration: duration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#duration ElasticsearchDomain#duration}
        :param start_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#start_at ElasticsearchDomain#start_at}.
        '''
        if isinstance(duration, dict):
            duration = ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration(**duration)
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule.__init__)
            check_type(argname="argument cron_expression_for_recurrence", value=cron_expression_for_recurrence, expected_type=type_hints["cron_expression_for_recurrence"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument start_at", value=start_at, expected_type=type_hints["start_at"])
        self._values: typing.Dict[str, typing.Any] = {
            "cron_expression_for_recurrence": cron_expression_for_recurrence,
            "duration": duration,
            "start_at": start_at,
        }

    @builtins.property
    def cron_expression_for_recurrence(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cron_expression_for_recurrence ElasticsearchDomain#cron_expression_for_recurrence}.'''
        result = self._values.get("cron_expression_for_recurrence")
        assert result is not None, "Required property 'cron_expression_for_recurrence' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration(
        self,
    ) -> "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration":
        '''duration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#duration ElasticsearchDomain#duration}
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast("ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration", result)

    @builtins.property
    def start_at(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#start_at ElasticsearchDomain#start_at}.'''
        result = self._values.get("start_at")
        assert result is not None, "Required property 'start_at' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#unit ElasticsearchDomain#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#value ElasticsearchDomain#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration.__init__)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#unit ElasticsearchDomain#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#value ElasticsearchDomain#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration]:
        return typing.cast(typing.Optional[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDuration")
    def put_duration(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#unit ElasticsearchDomain#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#value ElasticsearchDomain#value}.
        '''
        value_ = ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putDuration", [value_]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="duration")
    def duration(
        self,
    ) -> ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference:
        return typing.cast(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference, jsii.get(self, "duration"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cronExpressionForRecurrenceInput")
    def cron_expression_for_recurrence_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cronExpressionForRecurrenceInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="durationInput")
    def duration_input(
        self,
    ) -> typing.Optional[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration]:
        return typing.cast(typing.Optional[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration], jsii.get(self, "durationInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="startAtInput")
    def start_at_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startAtInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cronExpressionForRecurrence")
    def cron_expression_for_recurrence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cronExpressionForRecurrence"))

    @cron_expression_for_recurrence.setter
    def cron_expression_for_recurrence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference, "cron_expression_for_recurrence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronExpressionForRecurrence", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="startAt")
    def start_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startAt"))

    @start_at.setter
    def start_at(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference, "start_at").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startAt", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainAutoTuneOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainAutoTuneOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAutoTuneOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMaintenanceSchedule")
    def put_maintenance_schedule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainAutoTuneOptionsOutputReference.put_maintenance_schedule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMaintenanceSchedule", [value]))

    @jsii.member(jsii_name="resetMaintenanceSchedule")
    def reset_maintenance_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceSchedule", []))

    @jsii.member(jsii_name="resetRollbackOnDisable")
    def reset_rollback_on_disable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRollbackOnDisable", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maintenanceSchedule")
    def maintenance_schedule(
        self,
    ) -> ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList:
        return typing.cast(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList, jsii.get(self, "maintenanceSchedule"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maintenanceScheduleInput")
    def maintenance_schedule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]]], jsii.get(self, "maintenanceScheduleInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rollbackOnDisableInput")
    def rollback_on_disable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rollbackOnDisableInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsOutputReference, "desired_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rollbackOnDisable")
    def rollback_on_disable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rollbackOnDisable"))

    @rollback_on_disable.setter
    def rollback_on_disable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsOutputReference, "rollback_on_disable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rollbackOnDisable", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainAutoTuneOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainAutoTuneOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainAutoTuneOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainAutoTuneOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainClusterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cold_storage_options": "coldStorageOptions",
        "dedicated_master_count": "dedicatedMasterCount",
        "dedicated_master_enabled": "dedicatedMasterEnabled",
        "dedicated_master_type": "dedicatedMasterType",
        "instance_count": "instanceCount",
        "instance_type": "instanceType",
        "warm_count": "warmCount",
        "warm_enabled": "warmEnabled",
        "warm_type": "warmType",
        "zone_awareness_config": "zoneAwarenessConfig",
        "zone_awareness_enabled": "zoneAwarenessEnabled",
    },
)
class ElasticsearchDomainClusterConfig:
    def __init__(
        self,
        *,
        cold_storage_options: typing.Optional[typing.Union["ElasticsearchDomainClusterConfigColdStorageOptions", typing.Dict[str, typing.Any]]] = None,
        dedicated_master_count: typing.Optional[jsii.Number] = None,
        dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dedicated_master_type: typing.Optional[builtins.str] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        instance_type: typing.Optional[builtins.str] = None,
        warm_count: typing.Optional[jsii.Number] = None,
        warm_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        warm_type: typing.Optional[builtins.str] = None,
        zone_awareness_config: typing.Optional[typing.Union["ElasticsearchDomainClusterConfigZoneAwarenessConfig", typing.Dict[str, typing.Any]]] = None,
        zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cold_storage_options: cold_storage_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cold_storage_options ElasticsearchDomain#cold_storage_options}
        :param dedicated_master_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_count ElasticsearchDomain#dedicated_master_count}.
        :param dedicated_master_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_enabled ElasticsearchDomain#dedicated_master_enabled}.
        :param dedicated_master_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_type ElasticsearchDomain#dedicated_master_type}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_count ElasticsearchDomain#instance_count}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_type ElasticsearchDomain#instance_type}.
        :param warm_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_count ElasticsearchDomain#warm_count}.
        :param warm_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_enabled ElasticsearchDomain#warm_enabled}.
        :param warm_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_type ElasticsearchDomain#warm_type}.
        :param zone_awareness_config: zone_awareness_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_config ElasticsearchDomain#zone_awareness_config}
        :param zone_awareness_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_enabled ElasticsearchDomain#zone_awareness_enabled}.
        '''
        if isinstance(cold_storage_options, dict):
            cold_storage_options = ElasticsearchDomainClusterConfigColdStorageOptions(**cold_storage_options)
        if isinstance(zone_awareness_config, dict):
            zone_awareness_config = ElasticsearchDomainClusterConfigZoneAwarenessConfig(**zone_awareness_config)
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainClusterConfig.__init__)
            check_type(argname="argument cold_storage_options", value=cold_storage_options, expected_type=type_hints["cold_storage_options"])
            check_type(argname="argument dedicated_master_count", value=dedicated_master_count, expected_type=type_hints["dedicated_master_count"])
            check_type(argname="argument dedicated_master_enabled", value=dedicated_master_enabled, expected_type=type_hints["dedicated_master_enabled"])
            check_type(argname="argument dedicated_master_type", value=dedicated_master_type, expected_type=type_hints["dedicated_master_type"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument warm_count", value=warm_count, expected_type=type_hints["warm_count"])
            check_type(argname="argument warm_enabled", value=warm_enabled, expected_type=type_hints["warm_enabled"])
            check_type(argname="argument warm_type", value=warm_type, expected_type=type_hints["warm_type"])
            check_type(argname="argument zone_awareness_config", value=zone_awareness_config, expected_type=type_hints["zone_awareness_config"])
            check_type(argname="argument zone_awareness_enabled", value=zone_awareness_enabled, expected_type=type_hints["zone_awareness_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cold_storage_options is not None:
            self._values["cold_storage_options"] = cold_storage_options
        if dedicated_master_count is not None:
            self._values["dedicated_master_count"] = dedicated_master_count
        if dedicated_master_enabled is not None:
            self._values["dedicated_master_enabled"] = dedicated_master_enabled
        if dedicated_master_type is not None:
            self._values["dedicated_master_type"] = dedicated_master_type
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if warm_count is not None:
            self._values["warm_count"] = warm_count
        if warm_enabled is not None:
            self._values["warm_enabled"] = warm_enabled
        if warm_type is not None:
            self._values["warm_type"] = warm_type
        if zone_awareness_config is not None:
            self._values["zone_awareness_config"] = zone_awareness_config
        if zone_awareness_enabled is not None:
            self._values["zone_awareness_enabled"] = zone_awareness_enabled

    @builtins.property
    def cold_storage_options(
        self,
    ) -> typing.Optional["ElasticsearchDomainClusterConfigColdStorageOptions"]:
        '''cold_storage_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cold_storage_options ElasticsearchDomain#cold_storage_options}
        '''
        result = self._values.get("cold_storage_options")
        return typing.cast(typing.Optional["ElasticsearchDomainClusterConfigColdStorageOptions"], result)

    @builtins.property
    def dedicated_master_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_count ElasticsearchDomain#dedicated_master_count}.'''
        result = self._values.get("dedicated_master_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dedicated_master_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_enabled ElasticsearchDomain#dedicated_master_enabled}.'''
        result = self._values.get("dedicated_master_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def dedicated_master_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_type ElasticsearchDomain#dedicated_master_type}.'''
        result = self._values.get("dedicated_master_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_count ElasticsearchDomain#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_type ElasticsearchDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warm_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_count ElasticsearchDomain#warm_count}.'''
        result = self._values.get("warm_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warm_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_enabled ElasticsearchDomain#warm_enabled}.'''
        result = self._values.get("warm_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def warm_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_type ElasticsearchDomain#warm_type}.'''
        result = self._values.get("warm_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone_awareness_config(
        self,
    ) -> typing.Optional["ElasticsearchDomainClusterConfigZoneAwarenessConfig"]:
        '''zone_awareness_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_config ElasticsearchDomain#zone_awareness_config}
        '''
        result = self._values.get("zone_awareness_config")
        return typing.cast(typing.Optional["ElasticsearchDomainClusterConfigZoneAwarenessConfig"], result)

    @builtins.property
    def zone_awareness_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_enabled ElasticsearchDomain#zone_awareness_enabled}.'''
        result = self._values.get("zone_awareness_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainClusterConfigColdStorageOptions",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ElasticsearchDomainClusterConfigColdStorageOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainClusterConfigColdStorageOptions.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainClusterConfigColdStorageOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainClusterConfigColdStorageOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainClusterConfigColdStorageOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainClusterConfigColdStorageOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainClusterConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putColdStorageOptions")
    def put_cold_storage_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        value = ElasticsearchDomainClusterConfigColdStorageOptions(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putColdStorageOptions", [value]))

    @jsii.member(jsii_name="putZoneAwarenessConfig")
    def put_zone_awareness_config(
        self,
        *,
        availability_zone_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability_zone_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#availability_zone_count ElasticsearchDomain#availability_zone_count}.
        '''
        value = ElasticsearchDomainClusterConfigZoneAwarenessConfig(
            availability_zone_count=availability_zone_count
        )

        return typing.cast(None, jsii.invoke(self, "putZoneAwarenessConfig", [value]))

    @jsii.member(jsii_name="resetColdStorageOptions")
    def reset_cold_storage_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColdStorageOptions", []))

    @jsii.member(jsii_name="resetDedicatedMasterCount")
    def reset_dedicated_master_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDedicatedMasterCount", []))

    @jsii.member(jsii_name="resetDedicatedMasterEnabled")
    def reset_dedicated_master_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDedicatedMasterEnabled", []))

    @jsii.member(jsii_name="resetDedicatedMasterType")
    def reset_dedicated_master_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDedicatedMasterType", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetWarmCount")
    def reset_warm_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarmCount", []))

    @jsii.member(jsii_name="resetWarmEnabled")
    def reset_warm_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarmEnabled", []))

    @jsii.member(jsii_name="resetWarmType")
    def reset_warm_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarmType", []))

    @jsii.member(jsii_name="resetZoneAwarenessConfig")
    def reset_zone_awareness_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneAwarenessConfig", []))

    @jsii.member(jsii_name="resetZoneAwarenessEnabled")
    def reset_zone_awareness_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneAwarenessEnabled", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="coldStorageOptions")
    def cold_storage_options(
        self,
    ) -> ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference:
        return typing.cast(ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference, jsii.get(self, "coldStorageOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="zoneAwarenessConfig")
    def zone_awareness_config(
        self,
    ) -> "ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference":
        return typing.cast("ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference", jsii.get(self, "zoneAwarenessConfig"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="coldStorageOptionsInput")
    def cold_storage_options_input(
        self,
    ) -> typing.Optional[ElasticsearchDomainClusterConfigColdStorageOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainClusterConfigColdStorageOptions], jsii.get(self, "coldStorageOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedMasterCountInput")
    def dedicated_master_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dedicatedMasterCountInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedMasterEnabledInput")
    def dedicated_master_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dedicatedMasterEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedMasterTypeInput")
    def dedicated_master_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dedicatedMasterTypeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="warmCountInput")
    def warm_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "warmCountInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="warmEnabledInput")
    def warm_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "warmEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="warmTypeInput")
    def warm_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warmTypeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="zoneAwarenessConfigInput")
    def zone_awareness_config_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainClusterConfigZoneAwarenessConfig"]:
        return typing.cast(typing.Optional["ElasticsearchDomainClusterConfigZoneAwarenessConfig"], jsii.get(self, "zoneAwarenessConfigInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="zoneAwarenessEnabledInput")
    def zone_awareness_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "zoneAwarenessEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedMasterCount")
    def dedicated_master_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dedicatedMasterCount"))

    @dedicated_master_count.setter
    def dedicated_master_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigOutputReference, "dedicated_master_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dedicatedMasterCount", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedMasterEnabled")
    def dedicated_master_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dedicatedMasterEnabled"))

    @dedicated_master_enabled.setter
    def dedicated_master_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigOutputReference, "dedicated_master_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dedicatedMasterEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dedicatedMasterType")
    def dedicated_master_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dedicatedMasterType"))

    @dedicated_master_type.setter
    def dedicated_master_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigOutputReference, "dedicated_master_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dedicatedMasterType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigOutputReference, "instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigOutputReference, "instance_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="warmCount")
    def warm_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "warmCount"))

    @warm_count.setter
    def warm_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigOutputReference, "warm_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warmCount", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="warmEnabled")
    def warm_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "warmEnabled"))

    @warm_enabled.setter
    def warm_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigOutputReference, "warm_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warmEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="warmType")
    def warm_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warmType"))

    @warm_type.setter
    def warm_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigOutputReference, "warm_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warmType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="zoneAwarenessEnabled")
    def zone_awareness_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "zoneAwarenessEnabled"))

    @zone_awareness_enabled.setter
    def zone_awareness_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigOutputReference, "zone_awareness_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneAwarenessEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainClusterConfig]:
        return typing.cast(typing.Optional[ElasticsearchDomainClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainClusterConfigZoneAwarenessConfig",
    jsii_struct_bases=[],
    name_mapping={"availability_zone_count": "availabilityZoneCount"},
)
class ElasticsearchDomainClusterConfigZoneAwarenessConfig:
    def __init__(
        self,
        *,
        availability_zone_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability_zone_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#availability_zone_count ElasticsearchDomain#availability_zone_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainClusterConfigZoneAwarenessConfig.__init__)
            check_type(argname="argument availability_zone_count", value=availability_zone_count, expected_type=type_hints["availability_zone_count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if availability_zone_count is not None:
            self._values["availability_zone_count"] = availability_zone_count

    @builtins.property
    def availability_zone_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#availability_zone_count ElasticsearchDomain#availability_zone_count}.'''
        result = self._values.get("availability_zone_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainClusterConfigZoneAwarenessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailabilityZoneCount")
    def reset_availability_zone_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZoneCount", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZoneCountInput")
    def availability_zone_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "availabilityZoneCountInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZoneCount")
    def availability_zone_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "availabilityZoneCount"))

    @availability_zone_count.setter
    def availability_zone_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference, "availability_zone_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneCount", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainClusterConfigZoneAwarenessConfig]:
        return typing.cast(typing.Optional[ElasticsearchDomainClusterConfigZoneAwarenessConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainClusterConfigZoneAwarenessConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainCognitoOptions",
    jsii_struct_bases=[],
    name_mapping={
        "identity_pool_id": "identityPoolId",
        "role_arn": "roleArn",
        "user_pool_id": "userPoolId",
        "enabled": "enabled",
    },
)
class ElasticsearchDomainCognitoOptions:
    def __init__(
        self,
        *,
        identity_pool_id: builtins.str,
        role_arn: builtins.str,
        user_pool_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param identity_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#identity_pool_id ElasticsearchDomain#identity_pool_id}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#role_arn ElasticsearchDomain#role_arn}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#user_pool_id ElasticsearchDomain#user_pool_id}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainCognitoOptions.__init__)
            check_type(argname="argument identity_pool_id", value=identity_pool_id, expected_type=type_hints["identity_pool_id"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity_pool_id": identity_pool_id,
            "role_arn": role_arn,
            "user_pool_id": user_pool_id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def identity_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#identity_pool_id ElasticsearchDomain#identity_pool_id}.'''
        result = self._values.get("identity_pool_id")
        assert result is not None, "Required property 'identity_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#role_arn ElasticsearchDomain#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#user_pool_id ElasticsearchDomain#user_pool_id}.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainCognitoOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainCognitoOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainCognitoOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainCognitoOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityPoolIdInput")
    def identity_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityPoolIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userPoolIdInput")
    def user_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainCognitoOptionsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityPoolId")
    def identity_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityPoolId"))

    @identity_pool_id.setter
    def identity_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainCognitoOptionsOutputReference, "identity_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityPoolId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainCognitoOptionsOutputReference, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @user_pool_id.setter
    def user_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainCognitoOptionsOutputReference, "user_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainCognitoOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainCognitoOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainCognitoOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainCognitoOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain_name": "domainName",
        "access_policies": "accessPolicies",
        "advanced_options": "advancedOptions",
        "advanced_security_options": "advancedSecurityOptions",
        "auto_tune_options": "autoTuneOptions",
        "cluster_config": "clusterConfig",
        "cognito_options": "cognitoOptions",
        "domain_endpoint_options": "domainEndpointOptions",
        "ebs_options": "ebsOptions",
        "elasticsearch_version": "elasticsearchVersion",
        "encrypt_at_rest": "encryptAtRest",
        "id": "id",
        "log_publishing_options": "logPublishingOptions",
        "node_to_node_encryption": "nodeToNodeEncryption",
        "snapshot_options": "snapshotOptions",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "vpc_options": "vpcOptions",
    },
)
class ElasticsearchDomainConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]] = None,
        domain_name: builtins.str,
        access_policies: typing.Optional[builtins.str] = None,
        advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        advanced_security_options: typing.Optional[typing.Union[ElasticsearchDomainAdvancedSecurityOptions, typing.Dict[str, typing.Any]]] = None,
        auto_tune_options: typing.Optional[typing.Union[ElasticsearchDomainAutoTuneOptions, typing.Dict[str, typing.Any]]] = None,
        cluster_config: typing.Optional[typing.Union[ElasticsearchDomainClusterConfig, typing.Dict[str, typing.Any]]] = None,
        cognito_options: typing.Optional[typing.Union[ElasticsearchDomainCognitoOptions, typing.Dict[str, typing.Any]]] = None,
        domain_endpoint_options: typing.Optional[typing.Union["ElasticsearchDomainDomainEndpointOptions", typing.Dict[str, typing.Any]]] = None,
        ebs_options: typing.Optional[typing.Union["ElasticsearchDomainEbsOptions", typing.Dict[str, typing.Any]]] = None,
        elasticsearch_version: typing.Optional[builtins.str] = None,
        encrypt_at_rest: typing.Optional[typing.Union["ElasticsearchDomainEncryptAtRest", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        log_publishing_options: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElasticsearchDomainLogPublishingOptions", typing.Dict[str, typing.Any]]]]] = None,
        node_to_node_encryption: typing.Optional[typing.Union["ElasticsearchDomainNodeToNodeEncryption", typing.Dict[str, typing.Any]]] = None,
        snapshot_options: typing.Optional[typing.Union["ElasticsearchDomainSnapshotOptions", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ElasticsearchDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpc_options: typing.Optional[typing.Union["ElasticsearchDomainVpcOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''AWS ElasticSearch Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_name ElasticsearchDomain#domain_name}.
        :param access_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#access_policies ElasticsearchDomain#access_policies}.
        :param advanced_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_options ElasticsearchDomain#advanced_options}.
        :param advanced_security_options: advanced_security_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_security_options ElasticsearchDomain#advanced_security_options}
        :param auto_tune_options: auto_tune_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#auto_tune_options ElasticsearchDomain#auto_tune_options}
        :param cluster_config: cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cluster_config ElasticsearchDomain#cluster_config}
        :param cognito_options: cognito_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cognito_options ElasticsearchDomain#cognito_options}
        :param domain_endpoint_options: domain_endpoint_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_endpoint_options ElasticsearchDomain#domain_endpoint_options}
        :param ebs_options: ebs_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_options ElasticsearchDomain#ebs_options}
        :param elasticsearch_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#elasticsearch_version ElasticsearchDomain#elasticsearch_version}.
        :param encrypt_at_rest: encrypt_at_rest block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#encrypt_at_rest ElasticsearchDomain#encrypt_at_rest}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#id ElasticsearchDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_publishing_options: log_publishing_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#log_publishing_options ElasticsearchDomain#log_publishing_options}
        :param node_to_node_encryption: node_to_node_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#node_to_node_encryption ElasticsearchDomain#node_to_node_encryption}
        :param snapshot_options: snapshot_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#snapshot_options ElasticsearchDomain#snapshot_options}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags ElasticsearchDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags_all ElasticsearchDomain#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#timeouts ElasticsearchDomain#timeouts}
        :param vpc_options: vpc_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#vpc_options ElasticsearchDomain#vpc_options}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(advanced_security_options, dict):
            advanced_security_options = ElasticsearchDomainAdvancedSecurityOptions(**advanced_security_options)
        if isinstance(auto_tune_options, dict):
            auto_tune_options = ElasticsearchDomainAutoTuneOptions(**auto_tune_options)
        if isinstance(cluster_config, dict):
            cluster_config = ElasticsearchDomainClusterConfig(**cluster_config)
        if isinstance(cognito_options, dict):
            cognito_options = ElasticsearchDomainCognitoOptions(**cognito_options)
        if isinstance(domain_endpoint_options, dict):
            domain_endpoint_options = ElasticsearchDomainDomainEndpointOptions(**domain_endpoint_options)
        if isinstance(ebs_options, dict):
            ebs_options = ElasticsearchDomainEbsOptions(**ebs_options)
        if isinstance(encrypt_at_rest, dict):
            encrypt_at_rest = ElasticsearchDomainEncryptAtRest(**encrypt_at_rest)
        if isinstance(node_to_node_encryption, dict):
            node_to_node_encryption = ElasticsearchDomainNodeToNodeEncryption(**node_to_node_encryption)
        if isinstance(snapshot_options, dict):
            snapshot_options = ElasticsearchDomainSnapshotOptions(**snapshot_options)
        if isinstance(timeouts, dict):
            timeouts = ElasticsearchDomainTimeouts(**timeouts)
        if isinstance(vpc_options, dict):
            vpc_options = ElasticsearchDomainVpcOptions(**vpc_options)
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument access_policies", value=access_policies, expected_type=type_hints["access_policies"])
            check_type(argname="argument advanced_options", value=advanced_options, expected_type=type_hints["advanced_options"])
            check_type(argname="argument advanced_security_options", value=advanced_security_options, expected_type=type_hints["advanced_security_options"])
            check_type(argname="argument auto_tune_options", value=auto_tune_options, expected_type=type_hints["auto_tune_options"])
            check_type(argname="argument cluster_config", value=cluster_config, expected_type=type_hints["cluster_config"])
            check_type(argname="argument cognito_options", value=cognito_options, expected_type=type_hints["cognito_options"])
            check_type(argname="argument domain_endpoint_options", value=domain_endpoint_options, expected_type=type_hints["domain_endpoint_options"])
            check_type(argname="argument ebs_options", value=ebs_options, expected_type=type_hints["ebs_options"])
            check_type(argname="argument elasticsearch_version", value=elasticsearch_version, expected_type=type_hints["elasticsearch_version"])
            check_type(argname="argument encrypt_at_rest", value=encrypt_at_rest, expected_type=type_hints["encrypt_at_rest"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_publishing_options", value=log_publishing_options, expected_type=type_hints["log_publishing_options"])
            check_type(argname="argument node_to_node_encryption", value=node_to_node_encryption, expected_type=type_hints["node_to_node_encryption"])
            check_type(argname="argument snapshot_options", value=snapshot_options, expected_type=type_hints["snapshot_options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpc_options", value=vpc_options, expected_type=type_hints["vpc_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if access_policies is not None:
            self._values["access_policies"] = access_policies
        if advanced_options is not None:
            self._values["advanced_options"] = advanced_options
        if advanced_security_options is not None:
            self._values["advanced_security_options"] = advanced_security_options
        if auto_tune_options is not None:
            self._values["auto_tune_options"] = auto_tune_options
        if cluster_config is not None:
            self._values["cluster_config"] = cluster_config
        if cognito_options is not None:
            self._values["cognito_options"] = cognito_options
        if domain_endpoint_options is not None:
            self._values["domain_endpoint_options"] = domain_endpoint_options
        if ebs_options is not None:
            self._values["ebs_options"] = ebs_options
        if elasticsearch_version is not None:
            self._values["elasticsearch_version"] = elasticsearch_version
        if encrypt_at_rest is not None:
            self._values["encrypt_at_rest"] = encrypt_at_rest
        if id is not None:
            self._values["id"] = id
        if log_publishing_options is not None:
            self._values["log_publishing_options"] = log_publishing_options
        if node_to_node_encryption is not None:
            self._values["node_to_node_encryption"] = node_to_node_encryption
        if snapshot_options is not None:
            self._values["snapshot_options"] = snapshot_options
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpc_options is not None:
            self._values["vpc_options"] = vpc_options

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]], result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_name ElasticsearchDomain#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_policies(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#access_policies ElasticsearchDomain#access_policies}.'''
        result = self._values.get("access_policies")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def advanced_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_options ElasticsearchDomain#advanced_options}.'''
        result = self._values.get("advanced_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def advanced_security_options(
        self,
    ) -> typing.Optional[ElasticsearchDomainAdvancedSecurityOptions]:
        '''advanced_security_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_security_options ElasticsearchDomain#advanced_security_options}
        '''
        result = self._values.get("advanced_security_options")
        return typing.cast(typing.Optional[ElasticsearchDomainAdvancedSecurityOptions], result)

    @builtins.property
    def auto_tune_options(self) -> typing.Optional[ElasticsearchDomainAutoTuneOptions]:
        '''auto_tune_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#auto_tune_options ElasticsearchDomain#auto_tune_options}
        '''
        result = self._values.get("auto_tune_options")
        return typing.cast(typing.Optional[ElasticsearchDomainAutoTuneOptions], result)

    @builtins.property
    def cluster_config(self) -> typing.Optional[ElasticsearchDomainClusterConfig]:
        '''cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cluster_config ElasticsearchDomain#cluster_config}
        '''
        result = self._values.get("cluster_config")
        return typing.cast(typing.Optional[ElasticsearchDomainClusterConfig], result)

    @builtins.property
    def cognito_options(self) -> typing.Optional[ElasticsearchDomainCognitoOptions]:
        '''cognito_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cognito_options ElasticsearchDomain#cognito_options}
        '''
        result = self._values.get("cognito_options")
        return typing.cast(typing.Optional[ElasticsearchDomainCognitoOptions], result)

    @builtins.property
    def domain_endpoint_options(
        self,
    ) -> typing.Optional["ElasticsearchDomainDomainEndpointOptions"]:
        '''domain_endpoint_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_endpoint_options ElasticsearchDomain#domain_endpoint_options}
        '''
        result = self._values.get("domain_endpoint_options")
        return typing.cast(typing.Optional["ElasticsearchDomainDomainEndpointOptions"], result)

    @builtins.property
    def ebs_options(self) -> typing.Optional["ElasticsearchDomainEbsOptions"]:
        '''ebs_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_options ElasticsearchDomain#ebs_options}
        '''
        result = self._values.get("ebs_options")
        return typing.cast(typing.Optional["ElasticsearchDomainEbsOptions"], result)

    @builtins.property
    def elasticsearch_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#elasticsearch_version ElasticsearchDomain#elasticsearch_version}.'''
        result = self._values.get("elasticsearch_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypt_at_rest(self) -> typing.Optional["ElasticsearchDomainEncryptAtRest"]:
        '''encrypt_at_rest block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#encrypt_at_rest ElasticsearchDomain#encrypt_at_rest}
        '''
        result = self._values.get("encrypt_at_rest")
        return typing.cast(typing.Optional["ElasticsearchDomainEncryptAtRest"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#id ElasticsearchDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_publishing_options(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElasticsearchDomainLogPublishingOptions"]]]:
        '''log_publishing_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#log_publishing_options ElasticsearchDomain#log_publishing_options}
        '''
        result = self._values.get("log_publishing_options")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElasticsearchDomainLogPublishingOptions"]]], result)

    @builtins.property
    def node_to_node_encryption(
        self,
    ) -> typing.Optional["ElasticsearchDomainNodeToNodeEncryption"]:
        '''node_to_node_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#node_to_node_encryption ElasticsearchDomain#node_to_node_encryption}
        '''
        result = self._values.get("node_to_node_encryption")
        return typing.cast(typing.Optional["ElasticsearchDomainNodeToNodeEncryption"], result)

    @builtins.property
    def snapshot_options(self) -> typing.Optional["ElasticsearchDomainSnapshotOptions"]:
        '''snapshot_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#snapshot_options ElasticsearchDomain#snapshot_options}
        '''
        result = self._values.get("snapshot_options")
        return typing.cast(typing.Optional["ElasticsearchDomainSnapshotOptions"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags ElasticsearchDomain#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags_all ElasticsearchDomain#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ElasticsearchDomainTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#timeouts ElasticsearchDomain#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ElasticsearchDomainTimeouts"], result)

    @builtins.property
    def vpc_options(self) -> typing.Optional["ElasticsearchDomainVpcOptions"]:
        '''vpc_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#vpc_options ElasticsearchDomain#vpc_options}
        '''
        result = self._values.get("vpc_options")
        return typing.cast(typing.Optional["ElasticsearchDomainVpcOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainDomainEndpointOptions",
    jsii_struct_bases=[],
    name_mapping={
        "custom_endpoint": "customEndpoint",
        "custom_endpoint_certificate_arn": "customEndpointCertificateArn",
        "custom_endpoint_enabled": "customEndpointEnabled",
        "enforce_https": "enforceHttps",
        "tls_security_policy": "tlsSecurityPolicy",
    },
)
class ElasticsearchDomainDomainEndpointOptions:
    def __init__(
        self,
        *,
        custom_endpoint: typing.Optional[builtins.str] = None,
        custom_endpoint_certificate_arn: typing.Optional[builtins.str] = None,
        custom_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enforce_https: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_security_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint ElasticsearchDomain#custom_endpoint}.
        :param custom_endpoint_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_certificate_arn ElasticsearchDomain#custom_endpoint_certificate_arn}.
        :param custom_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_enabled ElasticsearchDomain#custom_endpoint_enabled}.
        :param enforce_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enforce_https ElasticsearchDomain#enforce_https}.
        :param tls_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tls_security_policy ElasticsearchDomain#tls_security_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainDomainEndpointOptions.__init__)
            check_type(argname="argument custom_endpoint", value=custom_endpoint, expected_type=type_hints["custom_endpoint"])
            check_type(argname="argument custom_endpoint_certificate_arn", value=custom_endpoint_certificate_arn, expected_type=type_hints["custom_endpoint_certificate_arn"])
            check_type(argname="argument custom_endpoint_enabled", value=custom_endpoint_enabled, expected_type=type_hints["custom_endpoint_enabled"])
            check_type(argname="argument enforce_https", value=enforce_https, expected_type=type_hints["enforce_https"])
            check_type(argname="argument tls_security_policy", value=tls_security_policy, expected_type=type_hints["tls_security_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_endpoint is not None:
            self._values["custom_endpoint"] = custom_endpoint
        if custom_endpoint_certificate_arn is not None:
            self._values["custom_endpoint_certificate_arn"] = custom_endpoint_certificate_arn
        if custom_endpoint_enabled is not None:
            self._values["custom_endpoint_enabled"] = custom_endpoint_enabled
        if enforce_https is not None:
            self._values["enforce_https"] = enforce_https
        if tls_security_policy is not None:
            self._values["tls_security_policy"] = tls_security_policy

    @builtins.property
    def custom_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint ElasticsearchDomain#custom_endpoint}.'''
        result = self._values.get("custom_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_endpoint_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_certificate_arn ElasticsearchDomain#custom_endpoint_certificate_arn}.'''
        result = self._values.get("custom_endpoint_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_endpoint_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_enabled ElasticsearchDomain#custom_endpoint_enabled}.'''
        result = self._values.get("custom_endpoint_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enforce_https(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enforce_https ElasticsearchDomain#enforce_https}.'''
        result = self._values.get("enforce_https")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_security_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tls_security_policy ElasticsearchDomain#tls_security_policy}.'''
        result = self._values.get("tls_security_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainDomainEndpointOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainDomainEndpointOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainDomainEndpointOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainDomainEndpointOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomEndpoint")
    def reset_custom_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomEndpoint", []))

    @jsii.member(jsii_name="resetCustomEndpointCertificateArn")
    def reset_custom_endpoint_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomEndpointCertificateArn", []))

    @jsii.member(jsii_name="resetCustomEndpointEnabled")
    def reset_custom_endpoint_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomEndpointEnabled", []))

    @jsii.member(jsii_name="resetEnforceHttps")
    def reset_enforce_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforceHttps", []))

    @jsii.member(jsii_name="resetTlsSecurityPolicy")
    def reset_tls_security_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsSecurityPolicy", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customEndpointCertificateArnInput")
    def custom_endpoint_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customEndpointCertificateArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customEndpointEnabledInput")
    def custom_endpoint_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "customEndpointEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customEndpointInput")
    def custom_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customEndpointInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enforceHttpsInput")
    def enforce_https_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enforceHttpsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tlsSecurityPolicyInput")
    def tls_security_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsSecurityPolicyInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customEndpoint")
    def custom_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customEndpoint"))

    @custom_endpoint.setter
    def custom_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainDomainEndpointOptionsOutputReference, "custom_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customEndpoint", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customEndpointCertificateArn")
    def custom_endpoint_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customEndpointCertificateArn"))

    @custom_endpoint_certificate_arn.setter
    def custom_endpoint_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainDomainEndpointOptionsOutputReference, "custom_endpoint_certificate_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customEndpointCertificateArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customEndpointEnabled")
    def custom_endpoint_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "customEndpointEnabled"))

    @custom_endpoint_enabled.setter
    def custom_endpoint_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainDomainEndpointOptionsOutputReference, "custom_endpoint_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customEndpointEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enforceHttps")
    def enforce_https(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enforceHttps"))

    @enforce_https.setter
    def enforce_https(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainDomainEndpointOptionsOutputReference, "enforce_https").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforceHttps", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tlsSecurityPolicy")
    def tls_security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsSecurityPolicy"))

    @tls_security_policy.setter
    def tls_security_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainDomainEndpointOptionsOutputReference, "tls_security_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsSecurityPolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainDomainEndpointOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainDomainEndpointOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainDomainEndpointOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainDomainEndpointOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainEbsOptions",
    jsii_struct_bases=[],
    name_mapping={
        "ebs_enabled": "ebsEnabled",
        "iops": "iops",
        "throughput": "throughput",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class ElasticsearchDomainEbsOptions:
    def __init__(
        self,
        *,
        ebs_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ebs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_enabled ElasticsearchDomain#ebs_enabled}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#iops ElasticsearchDomain#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#throughput ElasticsearchDomain#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_size ElasticsearchDomain#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_type ElasticsearchDomain#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainEbsOptions.__init__)
            check_type(argname="argument ebs_enabled", value=ebs_enabled, expected_type=type_hints["ebs_enabled"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "ebs_enabled": ebs_enabled,
        }
        if iops is not None:
            self._values["iops"] = iops
        if throughput is not None:
            self._values["throughput"] = throughput
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def ebs_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_enabled ElasticsearchDomain#ebs_enabled}.'''
        result = self._values.get("ebs_enabled")
        assert result is not None, "Required property 'ebs_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#iops ElasticsearchDomain#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#throughput ElasticsearchDomain#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_size ElasticsearchDomain#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_type ElasticsearchDomain#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainEbsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainEbsOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainEbsOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainEbsOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

    @jsii.member(jsii_name="resetVolumeSize")
    def reset_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeSize", []))

    @jsii.member(jsii_name="resetVolumeType")
    def reset_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeType", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ebsEnabledInput")
    def ebs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ebsEnabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeSizeInput")
    def volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeSizeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ebsEnabled")
    def ebs_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ebsEnabled"))

    @ebs_enabled.setter
    def ebs_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainEbsOptionsOutputReference, "ebs_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainEbsOptionsOutputReference, "iops").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainEbsOptionsOutputReference, "throughput").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainEbsOptionsOutputReference, "volume_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainEbsOptionsOutputReference, "volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainEbsOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainEbsOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainEbsOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainEbsOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainEncryptAtRest",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "kms_key_id": "kmsKeyId"},
)
class ElasticsearchDomainEncryptAtRest:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#kms_key_id ElasticsearchDomain#kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainEncryptAtRest.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#kms_key_id ElasticsearchDomain#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainEncryptAtRest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainEncryptAtRestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainEncryptAtRestOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainEncryptAtRestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainEncryptAtRestOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainEncryptAtRestOutputReference, "kms_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainEncryptAtRest]:
        return typing.cast(typing.Optional[ElasticsearchDomainEncryptAtRest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainEncryptAtRest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainEncryptAtRestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainLogPublishingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_log_group_arn": "cloudwatchLogGroupArn",
        "log_type": "logType",
        "enabled": "enabled",
    },
)
class ElasticsearchDomainLogPublishingOptions:
    def __init__(
        self,
        *,
        cloudwatch_log_group_arn: builtins.str,
        log_type: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cloudwatch_log_group_arn ElasticsearchDomain#cloudwatch_log_group_arn}.
        :param log_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#log_type ElasticsearchDomain#log_type}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainLogPublishingOptions.__init__)
            check_type(argname="argument cloudwatch_log_group_arn", value=cloudwatch_log_group_arn, expected_type=type_hints["cloudwatch_log_group_arn"])
            check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "cloudwatch_log_group_arn": cloudwatch_log_group_arn,
            "log_type": log_type,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def cloudwatch_log_group_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cloudwatch_log_group_arn ElasticsearchDomain#cloudwatch_log_group_arn}.'''
        result = self._values.get("cloudwatch_log_group_arn")
        assert result is not None, "Required property 'cloudwatch_log_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#log_type ElasticsearchDomain#log_type}.'''
        result = self._values.get("log_type")
        assert result is not None, "Required property 'log_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainLogPublishingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainLogPublishingOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainLogPublishingOptionsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainLogPublishingOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElasticsearchDomainLogPublishingOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainLogPublishingOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElasticsearchDomainLogPublishingOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainLogPublishingOptionsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainLogPublishingOptionsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainLogPublishingOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElasticsearchDomainLogPublishingOptions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElasticsearchDomainLogPublishingOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElasticsearchDomainLogPublishingOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainLogPublishingOptionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainLogPublishingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainLogPublishingOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainLogPublishingOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cloudwatchLogGroupArnInput")
    def cloudwatch_log_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudwatchLogGroupArnInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logTypeInput")
    def log_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logTypeInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLogGroupArn"))

    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainLogPublishingOptionsOutputReference, "cloudwatch_log_group_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchLogGroupArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainLogPublishingOptionsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logType")
    def log_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logType"))

    @log_type.setter
    def log_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainLogPublishingOptionsOutputReference, "log_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElasticsearchDomainLogPublishingOptions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElasticsearchDomainLogPublishingOptions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElasticsearchDomainLogPublishingOptions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainLogPublishingOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainNodeToNodeEncryption",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ElasticsearchDomainNodeToNodeEncryption:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainNodeToNodeEncryption.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainNodeToNodeEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainNodeToNodeEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainNodeToNodeEncryptionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainNodeToNodeEncryptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainNodeToNodeEncryptionOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainNodeToNodeEncryption]:
        return typing.cast(typing.Optional[ElasticsearchDomainNodeToNodeEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainNodeToNodeEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainNodeToNodeEncryptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy aws_elasticsearch_domain_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        access_policies: builtins.str,
        domain_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ElasticsearchDomainPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy aws_elasticsearch_domain_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param access_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#access_policies ElasticsearchDomainPolicy#access_policies}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#domain_name ElasticsearchDomainPolicy#domain_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#id ElasticsearchDomainPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#timeouts ElasticsearchDomainPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElasticsearchDomainPolicyConfig(
            access_policies=access_policies,
            domain_name=domain_name,
            id=id,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#delete ElasticsearchDomainPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#update ElasticsearchDomainPolicy#update}.
        '''
        value = ElasticsearchDomainPolicyTimeouts(delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ElasticsearchDomainPolicyTimeoutsOutputReference":
        return typing.cast("ElasticsearchDomainPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessPoliciesInput")
    def access_policies_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessPoliciesInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ElasticsearchDomainPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ElasticsearchDomainPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessPolicies")
    def access_policies(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessPolicies"))

    @access_policies.setter
    def access_policies(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainPolicy, "access_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPolicies", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainPolicy, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "access_policies": "accessPolicies",
        "domain_name": "domainName",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class ElasticsearchDomainPolicyConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]] = None,
        access_policies: builtins.str,
        domain_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ElasticsearchDomainPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''AWS ElasticSearch Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param access_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#access_policies ElasticsearchDomainPolicy#access_policies}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#domain_name ElasticsearchDomainPolicy#domain_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#id ElasticsearchDomainPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#timeouts ElasticsearchDomainPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ElasticsearchDomainPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument access_policies", value=access_policies, expected_type=type_hints["access_policies"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_policies": access_policies,
            "domain_name": domain_name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]], result)

    @builtins.property
    def access_policies(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#access_policies ElasticsearchDomainPolicy#access_policies}.'''
        result = self._values.get("access_policies")
        assert result is not None, "Required property 'access_policies' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#domain_name ElasticsearchDomainPolicy#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#id ElasticsearchDomainPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ElasticsearchDomainPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#timeouts ElasticsearchDomainPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ElasticsearchDomainPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"delete": "delete", "update": "update"},
)
class ElasticsearchDomainPolicyTimeouts:
    def __init__(
        self,
        *,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#delete ElasticsearchDomainPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#update ElasticsearchDomainPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainPolicyTimeouts.__init__)
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#delete ElasticsearchDomainPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy#update ElasticsearchDomainPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainPolicyTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainPolicyTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElasticsearchDomainPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElasticsearchDomainPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElasticsearchDomainPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainSamlOptions(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainSamlOptions",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options aws_elasticsearch_domain_saml_options}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        saml_options: typing.Optional[typing.Union["ElasticsearchDomainSamlOptionsSamlOptions", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["ElasticsearchDomainSamlOptionsTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options aws_elasticsearch_domain_saml_options} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#domain_name ElasticsearchDomainSamlOptions#domain_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#id ElasticsearchDomainSamlOptions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param saml_options: saml_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#saml_options ElasticsearchDomainSamlOptions#saml_options}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#timeouts ElasticsearchDomainSamlOptions#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainSamlOptions.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElasticsearchDomainSamlOptionsConfig(
            domain_name=domain_name,
            id=id,
            saml_options=saml_options,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSamlOptions")
    def put_saml_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        idp: typing.Optional[typing.Union["ElasticsearchDomainSamlOptionsSamlOptionsIdp", typing.Dict[str, typing.Any]]] = None,
        master_backend_role: typing.Optional[builtins.str] = None,
        master_user_name: typing.Optional[builtins.str] = None,
        roles_key: typing.Optional[builtins.str] = None,
        session_timeout_minutes: typing.Optional[jsii.Number] = None,
        subject_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#enabled ElasticsearchDomainSamlOptions#enabled}.
        :param idp: idp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#idp ElasticsearchDomainSamlOptions#idp}
        :param master_backend_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#master_backend_role ElasticsearchDomainSamlOptions#master_backend_role}.
        :param master_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#master_user_name ElasticsearchDomainSamlOptions#master_user_name}.
        :param roles_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#roles_key ElasticsearchDomainSamlOptions#roles_key}.
        :param session_timeout_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#session_timeout_minutes ElasticsearchDomainSamlOptions#session_timeout_minutes}.
        :param subject_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#subject_key ElasticsearchDomainSamlOptions#subject_key}.
        '''
        value = ElasticsearchDomainSamlOptionsSamlOptions(
            enabled=enabled,
            idp=idp,
            master_backend_role=master_backend_role,
            master_user_name=master_user_name,
            roles_key=roles_key,
            session_timeout_minutes=session_timeout_minutes,
            subject_key=subject_key,
        )

        return typing.cast(None, jsii.invoke(self, "putSamlOptions", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#delete ElasticsearchDomainSamlOptions#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#update ElasticsearchDomainSamlOptions#update}.
        '''
        value = ElasticsearchDomainSamlOptionsTimeouts(delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSamlOptions")
    def reset_saml_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSamlOptions", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="samlOptions")
    def saml_options(
        self,
    ) -> "ElasticsearchDomainSamlOptionsSamlOptionsOutputReference":
        return typing.cast("ElasticsearchDomainSamlOptionsSamlOptionsOutputReference", jsii.get(self, "samlOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ElasticsearchDomainSamlOptionsTimeoutsOutputReference":
        return typing.cast("ElasticsearchDomainSamlOptionsTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="samlOptionsInput")
    def saml_options_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainSamlOptionsSamlOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainSamlOptionsSamlOptions"], jsii.get(self, "samlOptionsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ElasticsearchDomainSamlOptionsTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ElasticsearchDomainSamlOptionsTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptions, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptions, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainSamlOptionsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain_name": "domainName",
        "id": "id",
        "saml_options": "samlOptions",
        "timeouts": "timeouts",
    },
)
class ElasticsearchDomainSamlOptionsConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]] = None,
        domain_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        saml_options: typing.Optional[typing.Union["ElasticsearchDomainSamlOptionsSamlOptions", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["ElasticsearchDomainSamlOptionsTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''AWS ElasticSearch Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#domain_name ElasticsearchDomainSamlOptions#domain_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#id ElasticsearchDomainSamlOptions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param saml_options: saml_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#saml_options ElasticsearchDomainSamlOptions#saml_options}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#timeouts ElasticsearchDomainSamlOptions#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(saml_options, dict):
            saml_options = ElasticsearchDomainSamlOptionsSamlOptions(**saml_options)
        if isinstance(timeouts, dict):
            timeouts = ElasticsearchDomainSamlOptionsTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainSamlOptionsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument saml_options", value=saml_options, expected_type=type_hints["saml_options"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id
        if saml_options is not None:
            self._values["saml_options"] = saml_options
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.ISSHProvisionerConnection, cdktf.IWinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.IFileProvisioner, cdktf.ILocalExecProvisioner, cdktf.IRemoteExecProvisioner]]], result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#domain_name ElasticsearchDomainSamlOptions#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#id ElasticsearchDomainSamlOptions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saml_options(
        self,
    ) -> typing.Optional["ElasticsearchDomainSamlOptionsSamlOptions"]:
        '''saml_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#saml_options ElasticsearchDomainSamlOptions#saml_options}
        '''
        result = self._values.get("saml_options")
        return typing.cast(typing.Optional["ElasticsearchDomainSamlOptionsSamlOptions"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ElasticsearchDomainSamlOptionsTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#timeouts ElasticsearchDomainSamlOptions#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ElasticsearchDomainSamlOptionsTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainSamlOptionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainSamlOptionsSamlOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "idp": "idp",
        "master_backend_role": "masterBackendRole",
        "master_user_name": "masterUserName",
        "roles_key": "rolesKey",
        "session_timeout_minutes": "sessionTimeoutMinutes",
        "subject_key": "subjectKey",
    },
)
class ElasticsearchDomainSamlOptionsSamlOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        idp: typing.Optional[typing.Union["ElasticsearchDomainSamlOptionsSamlOptionsIdp", typing.Dict[str, typing.Any]]] = None,
        master_backend_role: typing.Optional[builtins.str] = None,
        master_user_name: typing.Optional[builtins.str] = None,
        roles_key: typing.Optional[builtins.str] = None,
        session_timeout_minutes: typing.Optional[jsii.Number] = None,
        subject_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#enabled ElasticsearchDomainSamlOptions#enabled}.
        :param idp: idp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#idp ElasticsearchDomainSamlOptions#idp}
        :param master_backend_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#master_backend_role ElasticsearchDomainSamlOptions#master_backend_role}.
        :param master_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#master_user_name ElasticsearchDomainSamlOptions#master_user_name}.
        :param roles_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#roles_key ElasticsearchDomainSamlOptions#roles_key}.
        :param session_timeout_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#session_timeout_minutes ElasticsearchDomainSamlOptions#session_timeout_minutes}.
        :param subject_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#subject_key ElasticsearchDomainSamlOptions#subject_key}.
        '''
        if isinstance(idp, dict):
            idp = ElasticsearchDomainSamlOptionsSamlOptionsIdp(**idp)
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainSamlOptionsSamlOptions.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument idp", value=idp, expected_type=type_hints["idp"])
            check_type(argname="argument master_backend_role", value=master_backend_role, expected_type=type_hints["master_backend_role"])
            check_type(argname="argument master_user_name", value=master_user_name, expected_type=type_hints["master_user_name"])
            check_type(argname="argument roles_key", value=roles_key, expected_type=type_hints["roles_key"])
            check_type(argname="argument session_timeout_minutes", value=session_timeout_minutes, expected_type=type_hints["session_timeout_minutes"])
            check_type(argname="argument subject_key", value=subject_key, expected_type=type_hints["subject_key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if idp is not None:
            self._values["idp"] = idp
        if master_backend_role is not None:
            self._values["master_backend_role"] = master_backend_role
        if master_user_name is not None:
            self._values["master_user_name"] = master_user_name
        if roles_key is not None:
            self._values["roles_key"] = roles_key
        if session_timeout_minutes is not None:
            self._values["session_timeout_minutes"] = session_timeout_minutes
        if subject_key is not None:
            self._values["subject_key"] = subject_key

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#enabled ElasticsearchDomainSamlOptions#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def idp(self) -> typing.Optional["ElasticsearchDomainSamlOptionsSamlOptionsIdp"]:
        '''idp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#idp ElasticsearchDomainSamlOptions#idp}
        '''
        result = self._values.get("idp")
        return typing.cast(typing.Optional["ElasticsearchDomainSamlOptionsSamlOptionsIdp"], result)

    @builtins.property
    def master_backend_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#master_backend_role ElasticsearchDomainSamlOptions#master_backend_role}.'''
        result = self._values.get("master_backend_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#master_user_name ElasticsearchDomainSamlOptions#master_user_name}.'''
        result = self._values.get("master_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#roles_key ElasticsearchDomainSamlOptions#roles_key}.'''
        result = self._values.get("roles_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_timeout_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#session_timeout_minutes ElasticsearchDomainSamlOptions#session_timeout_minutes}.'''
        result = self._values.get("session_timeout_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def subject_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#subject_key ElasticsearchDomainSamlOptions#subject_key}.'''
        result = self._values.get("subject_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainSamlOptionsSamlOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainSamlOptionsSamlOptionsIdp",
    jsii_struct_bases=[],
    name_mapping={"entity_id": "entityId", "metadata_content": "metadataContent"},
)
class ElasticsearchDomainSamlOptionsSamlOptionsIdp:
    def __init__(
        self,
        *,
        entity_id: builtins.str,
        metadata_content: builtins.str,
    ) -> None:
        '''
        :param entity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#entity_id ElasticsearchDomainSamlOptions#entity_id}.
        :param metadata_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#metadata_content ElasticsearchDomainSamlOptions#metadata_content}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainSamlOptionsSamlOptionsIdp.__init__)
            check_type(argname="argument entity_id", value=entity_id, expected_type=type_hints["entity_id"])
            check_type(argname="argument metadata_content", value=metadata_content, expected_type=type_hints["metadata_content"])
        self._values: typing.Dict[str, typing.Any] = {
            "entity_id": entity_id,
            "metadata_content": metadata_content,
        }

    @builtins.property
    def entity_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#entity_id ElasticsearchDomainSamlOptions#entity_id}.'''
        result = self._values.get("entity_id")
        assert result is not None, "Required property 'entity_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metadata_content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#metadata_content ElasticsearchDomainSamlOptions#metadata_content}.'''
        result = self._values.get("metadata_content")
        assert result is not None, "Required property 'metadata_content' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainSamlOptionsSamlOptionsIdp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainSamlOptionsSamlOptionsIdpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainSamlOptionsSamlOptionsIdpOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainSamlOptionsSamlOptionsIdpOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="entityIdInput")
    def entity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityIdInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metadataContentInput")
    def metadata_content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataContentInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="entityId")
    def entity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityId"))

    @entity_id.setter
    def entity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsSamlOptionsIdpOutputReference, "entity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metadataContent")
    def metadata_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadataContent"))

    @metadata_content.setter
    def metadata_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsSamlOptionsIdpOutputReference, "metadata_content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadataContent", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainSamlOptionsSamlOptionsIdp]:
        return typing.cast(typing.Optional[ElasticsearchDomainSamlOptionsSamlOptionsIdp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainSamlOptionsSamlOptionsIdp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsSamlOptionsIdpOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainSamlOptionsSamlOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainSamlOptionsSamlOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainSamlOptionsSamlOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdp")
    def put_idp(
        self,
        *,
        entity_id: builtins.str,
        metadata_content: builtins.str,
    ) -> None:
        '''
        :param entity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#entity_id ElasticsearchDomainSamlOptions#entity_id}.
        :param metadata_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#metadata_content ElasticsearchDomainSamlOptions#metadata_content}.
        '''
        value = ElasticsearchDomainSamlOptionsSamlOptionsIdp(
            entity_id=entity_id, metadata_content=metadata_content
        )

        return typing.cast(None, jsii.invoke(self, "putIdp", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetIdp")
    def reset_idp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdp", []))

    @jsii.member(jsii_name="resetMasterBackendRole")
    def reset_master_backend_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterBackendRole", []))

    @jsii.member(jsii_name="resetMasterUserName")
    def reset_master_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterUserName", []))

    @jsii.member(jsii_name="resetRolesKey")
    def reset_roles_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRolesKey", []))

    @jsii.member(jsii_name="resetSessionTimeoutMinutes")
    def reset_session_timeout_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionTimeoutMinutes", []))

    @jsii.member(jsii_name="resetSubjectKey")
    def reset_subject_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectKey", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idp")
    def idp(self) -> ElasticsearchDomainSamlOptionsSamlOptionsIdpOutputReference:
        return typing.cast(ElasticsearchDomainSamlOptionsSamlOptionsIdpOutputReference, jsii.get(self, "idp"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idpInput")
    def idp_input(
        self,
    ) -> typing.Optional[ElasticsearchDomainSamlOptionsSamlOptionsIdp]:
        return typing.cast(typing.Optional[ElasticsearchDomainSamlOptionsSamlOptionsIdp], jsii.get(self, "idpInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterBackendRoleInput")
    def master_backend_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterBackendRoleInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserNameInput")
    def master_user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUserNameInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rolesKeyInput")
    def roles_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rolesKeyInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sessionTimeoutMinutesInput")
    def session_timeout_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionTimeoutMinutesInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subjectKeyInput")
    def subject_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectKeyInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsSamlOptionsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterBackendRole")
    def master_backend_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterBackendRole"))

    @master_backend_role.setter
    def master_backend_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsSamlOptionsOutputReference, "master_backend_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterBackendRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserName")
    def master_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterUserName"))

    @master_user_name.setter
    def master_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsSamlOptionsOutputReference, "master_user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rolesKey")
    def roles_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rolesKey"))

    @roles_key.setter
    def roles_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsSamlOptionsOutputReference, "roles_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rolesKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sessionTimeoutMinutes")
    def session_timeout_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionTimeoutMinutes"))

    @session_timeout_minutes.setter
    def session_timeout_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsSamlOptionsOutputReference, "session_timeout_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionTimeoutMinutes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subjectKey")
    def subject_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subjectKey"))

    @subject_key.setter
    def subject_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsSamlOptionsOutputReference, "subject_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainSamlOptionsSamlOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainSamlOptionsSamlOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainSamlOptionsSamlOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsSamlOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainSamlOptionsTimeouts",
    jsii_struct_bases=[],
    name_mapping={"delete": "delete", "update": "update"},
)
class ElasticsearchDomainSamlOptionsTimeouts:
    def __init__(
        self,
        *,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#delete ElasticsearchDomainSamlOptions#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#update ElasticsearchDomainSamlOptions#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainSamlOptionsTimeouts.__init__)
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#delete ElasticsearchDomainSamlOptions#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_saml_options#update ElasticsearchDomainSamlOptions#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainSamlOptionsTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainSamlOptionsTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainSamlOptionsTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainSamlOptionsTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElasticsearchDomainSamlOptionsTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElasticsearchDomainSamlOptionsTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElasticsearchDomainSamlOptionsTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSamlOptionsTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainSnapshotOptions",
    jsii_struct_bases=[],
    name_mapping={"automated_snapshot_start_hour": "automatedSnapshotStartHour"},
)
class ElasticsearchDomainSnapshotOptions:
    def __init__(self, *, automated_snapshot_start_hour: jsii.Number) -> None:
        '''
        :param automated_snapshot_start_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#automated_snapshot_start_hour ElasticsearchDomain#automated_snapshot_start_hour}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainSnapshotOptions.__init__)
            check_type(argname="argument automated_snapshot_start_hour", value=automated_snapshot_start_hour, expected_type=type_hints["automated_snapshot_start_hour"])
        self._values: typing.Dict[str, typing.Any] = {
            "automated_snapshot_start_hour": automated_snapshot_start_hour,
        }

    @builtins.property
    def automated_snapshot_start_hour(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#automated_snapshot_start_hour ElasticsearchDomain#automated_snapshot_start_hour}.'''
        result = self._values.get("automated_snapshot_start_hour")
        assert result is not None, "Required property 'automated_snapshot_start_hour' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainSnapshotOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainSnapshotOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainSnapshotOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainSnapshotOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="automatedSnapshotStartHourInput")
    def automated_snapshot_start_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "automatedSnapshotStartHourInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="automatedSnapshotStartHour")
    def automated_snapshot_start_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "automatedSnapshotStartHour"))

    @automated_snapshot_start_hour.setter
    def automated_snapshot_start_hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSnapshotOptionsOutputReference, "automated_snapshot_start_hour").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automatedSnapshotStartHour", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainSnapshotOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainSnapshotOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainSnapshotOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainSnapshotOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ElasticsearchDomainTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#create ElasticsearchDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#delete ElasticsearchDomain#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#update ElasticsearchDomain#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#create ElasticsearchDomain#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#delete ElasticsearchDomain#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#update ElasticsearchDomain#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElasticsearchDomainTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElasticsearchDomainTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElasticsearchDomainTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainVpcOptions",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class ElasticsearchDomainVpcOptions:
    def __init__(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#security_group_ids ElasticsearchDomain#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#subnet_ids ElasticsearchDomain#subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainVpcOptions.__init__)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[str, typing.Any] = {}
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#security_group_ids ElasticsearchDomain#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#subnet_ids ElasticsearchDomain#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainVpcOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainVpcOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elasticsearch.ElasticsearchDomainVpcOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElasticsearchDomainVpcOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainVpcOptionsOutputReference, "security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainVpcOptionsOutputReference, "subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainVpcOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainVpcOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainVpcOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElasticsearchDomainVpcOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAwsElasticsearchDomain",
    "DataAwsElasticsearchDomainAdvancedSecurityOptions",
    "DataAwsElasticsearchDomainAdvancedSecurityOptionsList",
    "DataAwsElasticsearchDomainAdvancedSecurityOptionsOutputReference",
    "DataAwsElasticsearchDomainAutoTuneOptions",
    "DataAwsElasticsearchDomainAutoTuneOptionsList",
    "DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceSchedule",
    "DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration",
    "DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationList",
    "DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference",
    "DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList",
    "DataAwsElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference",
    "DataAwsElasticsearchDomainAutoTuneOptionsOutputReference",
    "DataAwsElasticsearchDomainClusterConfig",
    "DataAwsElasticsearchDomainClusterConfigColdStorageOptions",
    "DataAwsElasticsearchDomainClusterConfigColdStorageOptionsList",
    "DataAwsElasticsearchDomainClusterConfigColdStorageOptionsOutputReference",
    "DataAwsElasticsearchDomainClusterConfigList",
    "DataAwsElasticsearchDomainClusterConfigOutputReference",
    "DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfig",
    "DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigList",
    "DataAwsElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference",
    "DataAwsElasticsearchDomainCognitoOptions",
    "DataAwsElasticsearchDomainCognitoOptionsList",
    "DataAwsElasticsearchDomainCognitoOptionsOutputReference",
    "DataAwsElasticsearchDomainConfig",
    "DataAwsElasticsearchDomainEbsOptions",
    "DataAwsElasticsearchDomainEbsOptionsList",
    "DataAwsElasticsearchDomainEbsOptionsOutputReference",
    "DataAwsElasticsearchDomainEncryptionAtRest",
    "DataAwsElasticsearchDomainEncryptionAtRestList",
    "DataAwsElasticsearchDomainEncryptionAtRestOutputReference",
    "DataAwsElasticsearchDomainLogPublishingOptions",
    "DataAwsElasticsearchDomainLogPublishingOptionsList",
    "DataAwsElasticsearchDomainLogPublishingOptionsOutputReference",
    "DataAwsElasticsearchDomainNodeToNodeEncryption",
    "DataAwsElasticsearchDomainNodeToNodeEncryptionList",
    "DataAwsElasticsearchDomainNodeToNodeEncryptionOutputReference",
    "DataAwsElasticsearchDomainSnapshotOptions",
    "DataAwsElasticsearchDomainSnapshotOptionsList",
    "DataAwsElasticsearchDomainSnapshotOptionsOutputReference",
    "DataAwsElasticsearchDomainVpcOptions",
    "DataAwsElasticsearchDomainVpcOptionsList",
    "DataAwsElasticsearchDomainVpcOptionsOutputReference",
    "ElasticsearchDomain",
    "ElasticsearchDomainAdvancedSecurityOptions",
    "ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions",
    "ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference",
    "ElasticsearchDomainAdvancedSecurityOptionsOutputReference",
    "ElasticsearchDomainAutoTuneOptions",
    "ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule",
    "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration",
    "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference",
    "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList",
    "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference",
    "ElasticsearchDomainAutoTuneOptionsOutputReference",
    "ElasticsearchDomainClusterConfig",
    "ElasticsearchDomainClusterConfigColdStorageOptions",
    "ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference",
    "ElasticsearchDomainClusterConfigOutputReference",
    "ElasticsearchDomainClusterConfigZoneAwarenessConfig",
    "ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference",
    "ElasticsearchDomainCognitoOptions",
    "ElasticsearchDomainCognitoOptionsOutputReference",
    "ElasticsearchDomainConfig",
    "ElasticsearchDomainDomainEndpointOptions",
    "ElasticsearchDomainDomainEndpointOptionsOutputReference",
    "ElasticsearchDomainEbsOptions",
    "ElasticsearchDomainEbsOptionsOutputReference",
    "ElasticsearchDomainEncryptAtRest",
    "ElasticsearchDomainEncryptAtRestOutputReference",
    "ElasticsearchDomainLogPublishingOptions",
    "ElasticsearchDomainLogPublishingOptionsList",
    "ElasticsearchDomainLogPublishingOptionsOutputReference",
    "ElasticsearchDomainNodeToNodeEncryption",
    "ElasticsearchDomainNodeToNodeEncryptionOutputReference",
    "ElasticsearchDomainPolicy",
    "ElasticsearchDomainPolicyConfig",
    "ElasticsearchDomainPolicyTimeouts",
    "ElasticsearchDomainPolicyTimeoutsOutputReference",
    "ElasticsearchDomainSamlOptions",
    "ElasticsearchDomainSamlOptionsConfig",
    "ElasticsearchDomainSamlOptionsSamlOptions",
    "ElasticsearchDomainSamlOptionsSamlOptionsIdp",
    "ElasticsearchDomainSamlOptionsSamlOptionsIdpOutputReference",
    "ElasticsearchDomainSamlOptionsSamlOptionsOutputReference",
    "ElasticsearchDomainSamlOptionsTimeouts",
    "ElasticsearchDomainSamlOptionsTimeoutsOutputReference",
    "ElasticsearchDomainSnapshotOptions",
    "ElasticsearchDomainSnapshotOptionsOutputReference",
    "ElasticsearchDomainTimeouts",
    "ElasticsearchDomainTimeoutsOutputReference",
    "ElasticsearchDomainVpcOptions",
    "ElasticsearchDomainVpcOptionsOutputReference",
]

publication.publish()
