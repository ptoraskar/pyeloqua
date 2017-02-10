CONTACT_SYSTEM_FIELDS = {
    "contactID": "{{Contact.Id}}",
    "createdAt": "{{Contact.CreatedAt}}",
    "updatedAt": "{{Contact.UpdatedAt}}",
    "isSubscribed": "{{Contact.Email.IsSubscribed}}",
    "isBounced": "{{Contact.Email.IsBounced}}"
}

ACTIVITY_FIELDS = {
    "EmailOpen": {
        "ActivityId": "{{Activity.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "EmailAddress": "{{Activity.Field(EmailAddress)}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "IpAddress": "{{Activity.Field(IpAddress)}}",
        "VisitorId": "{{Activity.Visitor.Id}}",
        "EmailRecipientId": "{{Activity.Field(EmailRecipientId)}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "SubjectLine": "{{Activity.Field(SubjectLine)}}",
        "EmailWebLink": "{{Activity.Field(EmailWebLink)}}",
        "VisitorExternalId": "{{Activity.Visitor.ExternalId}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}",
        "DeploymentId": "{{Activity.Field(EmailDeploymentId)}}",
        "EmailSendType": "{{Activity.Field(EmailSendType)}}"
    },
    "EmailClickthrough": {
        "ActivityId": "{{Activity.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "EmailAddress": "{{Activity.Field(EmailAddress)}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "IpAddress": "{{Activity.Field(IpAddress)}}",
        "VisitorId": "{{Activity.Visitor.Id}}",
        "EmailRecipientId": "{{Activity.Field(EmailRecipientId)}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "SubjectLine": "{{Activity.Field(SubjectLine)}}",
        "EmailWebLink": "{{Activity.Field(EmailWebLink)}}",
        "EmailClickedThruLink": "{{Activity.Field(EmailClickedThruLink)}}",
        "VisitorExternalId": "{{Activity.Visitor.ExternalId}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}",
        "DeploymentId": "{{Activity.Field(EmailDeploymentId)}}",
        "EmailSendType": "{{Activity.Field(EmailSendType)}}"
    },
    "EmailSend": {
        "ActivityId": "{{Activity.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "EmailAddress": "{{Activity.Field(EmailAddress)}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "EmailRecipientId": "{{Activity.Field(EmailRecipientId)}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "SubjectLine": "{{Activity.Field(SubjectLine)}}",
        "EmailWebLink": "{{Activity.Field(EmailWebLink)}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}",
        "DeploymentId": "{{Activity.Field(EmailDeploymentId)}}",
        "EmailSendType": "{{Activity.Field(EmailSendType)}}"
    },
    "Subscribe": {
        "ActivityId": "{{Activity.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "EmailAddress": "{{Activity.Field(EmailAddress)}}",
        "EmailRecipientId": "{{Activity.Field(EmailRecipientId)}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}"
    },
    "Unsubscribe": {
        "ActivityId": "{{Activity.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "EmailAddress": "{{Activity.Field(EmailAddress)}}",
        "EmailRecipientId": "{{Activity.Field(EmailRecipientId)}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}"
    },
    "Bounceback": {
        "ActivityId": "{{Activity.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "EmailAddress": "{{Activity.Field(EmailAddress)}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}"
    },
    "WebVisit": {
        "ActivityId": "{{Activity.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "VisitorId": "{{Activity.Visitor.Id}}",
        "VisitorExternalId": "{{Activity.Visitor.ExternalId}}",
        "ReferrerUrl": "{{Activity.Field(ReferrerUrl)}}",
        "IpAddress": "{{Activity.Field(IpAddress)}}",
        "NumberOfPages": "{{Activity.Field(NumberOfPages)}}",
        "FirstPageViewUrl": "{{Activity.Field(FirstPageViewUrl)}}",
        "Duration": "{{Activity.Field(Duration)}}",
        "ExternalId": "{{Activity.ExternalId}}"
    },
    "PageView": {
        "ActivityId": "{{Activity.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "VisitorId": "{{Activity.Visitor.Id}}",
        "VisitorExternalId": "{{Activity.Visitor.ExternalId}}",
        "WebVisitId": "{{Activity.Field(WebVisitId)}}",
        "Url": "{{Activity.Field(Url)}}",
        "ReferrerUrl": "{{Activity.Field(ReferrerUrl)}}",
        "IpAddress": "{{Activity.Field(IpAddress)}}",
        "IsWebTrackingOptedIn": "{{Activity.Field(IsWebTrackingOptedIn)}}",
        "ExternalId": "{{Activity.ExternalId}}"
    },
    "FormSubmit": {
        "ActivityId": "{{Activity.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "VisitorId": "{{Activity.Visitor.Id}}",
        "VisitorExternalId": "{{Activity.Visitor.ExternalId}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "RawData": "{{Activity.Field(RawData)}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}"
    },
    "External": {
        "C_EmailAddress": "{{Activity.Contact.Field(C_EmailAddress)}}",
        "CampaignID": "{{Activity.Campaign.Id}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetDate": "{{Activity.CreatedAt}}",
        "ActivityType": "{{Activity.Type}}"
    },
    "CommonFields": {
        "ActivityId": "{{Activity.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}"
    }
}
