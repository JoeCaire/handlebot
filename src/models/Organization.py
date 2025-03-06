import psycopg2
from src.interfaces.database.select import get_organization_by_sid, is_organization_registered
from src.interfaces.restAPI.scAPI import get_organization

class Organization:
    def __init__(self, organizationSID, name, logo, memberCount, recruiting, archetype, commitment, roleplay, primaryFocus, primaryImage, secondaryFocus, secondaryImage, banner, headline, langID):
        self.organizationSID = organizationSID
        self.name = name
        self.logo = logo
        self.memberCount = memberCount
        self.recruiting = recruiting
        self.archetype = archetype
        self.commitment = commitment
        self.roleplay = roleplay
        self.primaryFocus = primaryFocus
        self.primaryImage = primaryImage
        self.secondaryFocus = secondaryFocus
        self.secondaryImage = secondaryImage
        self.banner = banner
        self.headline = headline
        self.langID = langID
        self.lang = None

    @staticmethod
    def tryGetOrganizationFromSID(organizationSID):
        if is_organization_registered(organizationSID):
            return get_organization_by_sid(organizationSID)
        else:
            organization_data = get_organization(organizationSID)
            if organization_data:
                return organization_data
