import psycopg2

def insert_user(user):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        insert_query = """INSERT INTO users (userID, discordID, handle, displayName, organizationSID, organizationRank, enlisted, avatarURL, badge, badgeImage, bio, pageTitle, pageLink, country, region, website, referral, referralPrint) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (user.userID, user.discordID, user.handle, user.displayName, user.organizationSID, user.organizationRank, user.enlisted, user.avatarURL, user.badge, user.badgeImage, user.bio, user.pageTitle, user.pageLink, user.country, user.region, user.website, user.referral, user.referralPrint)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into users table")
    except (Exception, psycopg2.Error) as error:
        print("Error while inserting record into users table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_organization(organization):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        insert_query = """INSERT INTO organizations (organizationSID, name, logo, memberCount, recruiting, archetype, commitment, roleplay, primaryFocus, primaryImage, secondaryFocus, secondaryImage, banner, headline, langID) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (organization.organizationSID, organization.name, organization.logo, organization.memberCount, organization.recruiting, organization.archetype, organization.commitment, organization.roleplay, organization.primaryFocus, organization.primaryImage, organization.secondaryFocus, organization.secondaryImage, organization.banner, organization.headline, organization.langID)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into organizations table")
    except (Exception, psycopg2.Error) as error:
        print("Error while inserting record into organizations table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_guild(guild):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        insert_query = """INSERT INTO Server (guildID, prefix, langID, name, memberCount) 
                          VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (guild.guildID, guild.prefix, guild.langID, guild.name, guild.memberCount)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into Server table")
    except (Exception, psycopg2.Error) as error:
        print("Error while inserting record into Server table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
