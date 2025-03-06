class User:
    def __init__(self, userID, discordID, handle, displayName, organizationSID, organizationRank, enlisted, avatarURL, badge, badgeImage, bio, pageTitle, pageLink, country, region, website, referral, referralPrint):
        self.userID = userID
        self.discordID = discordID
        self.handle = handle
        self.displayName = displayName
        self.organizationSID = organizationSID
        self.organizationRank = organizationRank
        self.enlisted = enlisted
        self.avatarURL = avatarURL
        self.badge = badge
        self.badgeImage = badgeImage
        self.bio = bio
        self.pageTitle = pageTitle
        self.pageLink = pageLink
        self.country = country
        self.region = region
        self.website = website
        self.referral = referral
        self.referralPrint = referralPrint

    @staticmethod
    def tryGetUserFromDiscord(discord_id):
        # Implement the logic to fetch user data from the database using the provided Discord ID
        pass

    @staticmethod
    def tryGetUserFromHandle(handle, update=False):
        # Implement the logic to fetch user data from the database using the provided handle
        pass
