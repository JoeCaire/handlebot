import psycopg2

def update_user(user):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        update_query = """UPDATE users SET discordID = %s, handle = %s, displayName = %s, organizationSID = %s, organizationRank = %s, enlisted = %s, avatarURL = %s, badge = %s, badgeImage = %s, bio = %s, pageTitle = %s, pageLink = %s, country = %s, region = %s, website = %s, referral = %s, referralPrint = %s WHERE userID = %s"""
        record_to_update = (user.discordID, user.handle, user.displayName, user.organizationSID, user.organizationRank, user.enlisted, user.avatarURL, user.badge, user.badgeImage, user.bio, user.pageTitle, user.pageLink, user.country, user.region, user.website, user.referral, user.referralPrint, user.userID)
        cursor.execute(update_query, record_to_update)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully in users table")
    except (Exception, psycopg2.Error) as error:
        print("Error while updating record in users table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def update_organization(organization):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        update_query = """UPDATE organizations SET name = %s, logo = %s, memberCount = %s, recruiting = %s, archetype = %s, commitment = %s, roleplay = %s, primaryFocus = %s, primaryImage = %s, secondaryFocus = %s, secondaryImage = %s, banner = %s, headline = %s, langID = %s WHERE organizationSID = %s"""
        record_to_update = (organization.name, organization.logo, organization.memberCount, organization.recruiting, organization.archetype, organization.commitment, organization.roleplay, organization.primaryFocus, organization.primaryImage, organization.secondaryFocus, organization.secondaryImage, organization.banner, organization.headline, organization.langID, organization.organizationSID)
        cursor.execute(update_query, record_to_update)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully in organizations table")
    except (Exception, psycopg2.Error) as error:
        print("Error while updating record in organizations table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def update_guild(guild):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        update_query = """UPDATE Server SET prefix = %s, langID = %s, name = %s, memberCount = %s WHERE guildID = %s"""
        record_to_update = (guild.prefix, guild.langID, guild.name, guild.memberCount, guild.guildID)
        cursor.execute(update_query, record_to_update)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully in Server table")
    except (Exception, psycopg2.Error) as error:
        print("Error while updating record in Server table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
